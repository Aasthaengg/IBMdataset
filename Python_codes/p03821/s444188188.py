from itertools import accumulate
n = int(input())
lis = []
al=[]
bl=[]
for i in range(n):
    a,b=map(int, input().split())
    c=b-a%b
    al.append(a)
    bl.append(b)
ans=0
for i in range(n-1, -1, -1):
    if bl[i]==1:
        continue
    if (al[i]+ans)%bl[i]!=0:
        c=bl[i]-((al[i]+ans)%bl[i])
        ans+=c

print(ans)
