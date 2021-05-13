from collections import namedtuple
from functools import partial
from operator import attrgetter

Path = namedtuple('Path', ('length', 'left_seat', 'right_seat'))

m = set()
f = set()


def is_suitable_path(p: 'Path', m: 'set', f: 'set') -> 'bool':
    if p.length <= 1:
        return False
    if p.length % 2 == 0:
        return (p.left_seat in m and p.right_seat in f) or (p.left_seat in f and p.right_seat in m)
    else:
        return (p.left_seat in m and p.right_seat in m) or (p.left_seat in f and p.right_seat in f)


is_suitable_path = partial(is_suitable_path, m=m, f=f)

n = int(input())

checked = [n]
x = 0
for _ in range(20):
    print(x, flush=True)

    checked.append(x)
    checked.sort()

    res = input()
    if res[0] == 'V':
        break
    else:
        if res[0] == 'M':
            m.add(x)
            if x == 0:
                m.add(n)
        else:
            f.add(x)
            if x == 0:
                f.add(n)

        t = sorted(filter(is_suitable_path,
                          (Path(length=t - s, left_seat=s, right_seat=t) for s, t in zip(checked, checked[1:]))),
                   key=attrgetter('length'))
        x = (t[0].left_seat + t[0].right_seat) // 2
