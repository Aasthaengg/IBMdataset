s=list(input())
t=list(input())
if len(t)>len(s):
    print("UNRESTORABLE")
    exit()
n=len(s)
m=len(t)
ans=[]
for i in range(n-m+1):
    x=s.copy()
    f=0
    for j in range(m):
        if x[i+j]==t[j]:
            f+=1
        elif x[i+j]=="?":
            x[i+j]=t[j]
            f+=1
    if f==m:
        for j in range(n):
            if x[j]=="?":
                x[j]="a"
        ans.append("".join(x))
if len(ans)==0:
    print("UNRESTORABLE")
else:
    ans=sorted(ans)
    print(ans[0])
