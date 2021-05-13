n,t=map(int,input().split())
ct=[]
ans=[]
for i in range(n):
    ct=[int(x) for x in input().split()]
    if ct[1] <=t:
        ans.append(ct[0])
if ans==[]:
    print("TLE")
else:
    print(min(ans))

