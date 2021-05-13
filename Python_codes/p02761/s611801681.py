import sys
n,m=map(int,input().split())
ans=[0]*n
for _ in range(m):
    s,c=map(int,input().split())
    if ans[s-1]!=0 and ans[s-1]!=c:
        print(-1)
        sys.exit()
    if s==1 and c==0 and n!=1:
        print(-1)
        sys.exit()
    ans[s-1]=c
if ans[0]==0 and n!=1:
    ans[0]=1
num=0
for i in range(n):
    num+=ans[i]*(10**(n-i-1))
print(num)