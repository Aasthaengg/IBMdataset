import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
x = 1
ans = 0
while x**2<=N:
    if N%x==0:
        div = N//x
        if div-1>x:
            ans += div-1
    x += 1

print(ans)