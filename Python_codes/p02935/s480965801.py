import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input().rstrip())
v=sorted([int(i) for i in input().split()])
ans=v[0]
for i in range(1,n):
    ans=(ans+v[i])/2
print(ans)