n,q=map(int,input().split())
s=input()
ans,c=[0]*q,[0]*n
k=0
for i in range(1,n):
    if s[i-1]=="A" and s[i]=="C":
        k+=1
    c[i]=k

for i in range(q):
    l,r=map(int,input().split())
    ans[i]=c[r-1]-c[l-1]
for i in ans:
    print(i)
