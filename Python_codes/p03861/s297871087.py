import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))


a, b, x = LI()
acnt = (a - 1) // x
bcnt = b // x
ans = bcnt - acnt
print(ans)
