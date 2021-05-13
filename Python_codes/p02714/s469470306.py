n=int(input())
s=input()
r=s.count("R")
g=s.count("G")
b=s.count("B")
ans=r*g*b
for i in range(n):
    a=s[i]
    for j in range(i+1,n):
        b=s[j]
        d=j-i
        if j+d>=n:
            break
        c=s[j+d]
        if a!=b and b!=c and c!=a:
            ans-=1
print(ans)