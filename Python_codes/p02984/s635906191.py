import sys
sys.setrecursionlimit(10000000)
input=sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

res=[0]*n

res[0] = sum(a) - 2*sum(a[1::2])

for i in range(1,n):
    res[i] = 2*a[i-1] - res[i-1]

print(*res)