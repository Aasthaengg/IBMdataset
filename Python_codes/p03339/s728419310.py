n=int(input())
s=list(input())
e=s.count("E")
w=n-e
ans=e
nume=0
numw=0
for i in range(n):
    if s[i]=="E":
        nume+=1
    else:
        numw+=1
    ans=min(ans,numw+e-nume)
print(ans)
