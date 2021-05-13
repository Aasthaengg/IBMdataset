from copy import copy
s = input()
n=len(s)
x, y = map(int, input().split())

d = [len(v) for v in s.split("T")]
x -= d[0]
a = d[2::2]
b = d[1::2]


def c(d, x):
    cur = {0}
    for i in d:
        nxt = set()
        for j in cur:
            nxt.add(j + i)
            nxt.add(j - i)
        cur = copy(nxt)
    return x in cur

print("Yes" if c(a, x) and c(b, y) else "No")