t=input()
n=len(t)
ans=0
s=0
for i in range(n):
    if t[i]=="S":
        s+=1
    if s>0 and t[i]=="T":
        ans+=1
        s-=1
print(n-2*ans)