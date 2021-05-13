import sys
input = sys.stdin.readline
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
b=sorted([v[0]+v[1] for v in a],reverse=1)
ans=0
for i in a:
    ans-=i[1]
for i in range(n):
    if i%2==0:
        ans+=b[i]
print(ans)