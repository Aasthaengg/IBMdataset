s=input()
n=len(s)
now=0
ans=0
for  i in range(n):
    if s[i]=="W":ans+=i-now;now+=1
print(ans)