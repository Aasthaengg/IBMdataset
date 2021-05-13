n=int(input())
s1=input()
s2=input()
g=["c"]
i=0
while i<n:
    if s1[i]==s2[i]:
        g.append("a")
        i+=1
    else:
        g.append("b")
        i+=2
ans=1
mod=10**9+7
for i in range(len(g)-1):
    if g[i]=="c":
        if g[i+1]=="a":
            ans=(ans*3)%mod
        else:
            ans=(ans*6)%mod
    elif g[i]=="a":
        ans=(ans*2)%mod
    else:
        if g[i+1]=="b":
            ans=(ans*3)%mod
print(ans)