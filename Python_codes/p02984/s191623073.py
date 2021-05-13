import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))
#n, m = map(int, input().split())
#s = input()
#s,t = input().split()
#
#readline = sys.stdin.readline
#n,m = [int(i) for i in readline().split()]
#ab = [[int(i) for i in readline().split()] for _ in range(n)]

x2 = 0
for i in range(n):
    if i%2:
        x2 -= a[i]
    else:
        x2 += a[i]

ans = [0]*n
ans[0] = x2//2

for i in range(n-1):
    ans[i+1] = a[i] - ans[i]
    
for i in range(n):
    ans[i] *= 2
    
print(*ans)