import sys
input=sys.stdin.readline
h,w,n=map(int,input().split())
z=(h-2)*(w-2)
p=[]
for i in range(n):
    x,y=map(int,input().split())
    for j in range(3):
        for k in range(3):
            p.append([x+j-1,y+k-1])
p.sort(key=lambda x:(10**10)*x[0]+x[1])
n=len(p)
p.append([10**20,10**20])
ans=[0]*10
f=1
for i in range(n):
    if 2<=p[i][0]<=h-1 and 2<=p[i][1]<=w-1:
        if p[i]==p[i+1]:
            f+=1
        else:
            ans[f]+=1
            f=1
ans[0]=z-sum(ans)
for i in ans:
    print(i)
