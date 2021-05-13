S=input().replace("BC","D").split("B")
T=[]
for t in S:
    for u in t.split("C"):
        T.append(u)
#print(T)
ans=0
for s in T:
    n=len(s)
    k=0
    for i in range(n):
        if s[i]=="D":
            ans+=(i-k)
            k+=1
print(ans)