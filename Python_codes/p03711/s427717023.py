xy=list(map(int,input().split()))
alist=[1,3,5,7,8,10,12]
blist=[4,6,9,11]
clist=[2]
ans=[]

for i in xy:
    if i in alist:
        ans.append(0)
    if i in blist:
        ans.append(1)
    if i in clist:
        ans.append(2)

if ans[0]==ans[1]:
    print("Yes")
else:print("No")