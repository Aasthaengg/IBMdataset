import sys
from collections import deque
from itertools import islice
from operator import itemgetter


def resolve(in_):
    N, D, A = map(int, next(in_).split())
    def f(line):
        x, h = map(int, line.split())
        return x, (h + A - 1) // A
    XH = list(map(f, islice(in_, N)))
    XH.sort(key=itemgetter(0))
    assert N == len(XH)

    bomb_attack = deque()
    bomb = 0
    ans = 0
    for x, h in XH:
        while bomb_attack and bomb_attack[0][0] < x:
            e = bomb_attack.popleft()
            bomb -= e[1]

        h_real = h - bomb
        if h_real <= 0:
            continue
        ans += h_real
        bomb_attack.append((x + D * 2, h_real))
        bomb += h_real

    return ans


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
