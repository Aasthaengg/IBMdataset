import sys
input = sys.stdin.readline

n,m=map(int,input().split())
ans=0;wrong=0
d=[0]*n
for i in range(m):
    p,s=input().strip().split()
    p=int(p)-1
    if d[p]!=-1:
        if s=='WA':
            d[p]+=1
        else:
            wrong+=d[p]
            d[p]=-1
            ans+=1
print(ans,wrong)
