from operator import xor
from functools import reduce


def resolve():
    s, t = input().split()
    a, b = map(int, input().split())
    d = {s: a, t: b}
    u = input()
    d[u] -= 1
    print(d[s], d[t])

if __name__ == "__main__":
    resolve()
