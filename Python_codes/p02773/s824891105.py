n=int(input())
ans={"b":0}
ma=0
pr=[]
for i in range(n):
    name=input()
    if name in ans.keys():
        ans[name]=ans[name]+1
    else:
        ans[name]=1
for j,k in ans.items():
    if k>ma:
        ma=k 
        pr=[j]
    elif k==ma:
        pr.append(j)
pr.sort()
for l in pr:
    print(l)