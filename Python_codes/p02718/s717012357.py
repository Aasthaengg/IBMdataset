r=input().split()
N=int(r[0])
M=int(r[1])
d_pre=input().split()
d=[int(s) for s in d_pre]
x=sum(d)
ans=0
for i in range(N):
    if d[i]>=x/(4*M):
        ans+=1
if ans>=M:
    print("Yes")
else:
    print("No")