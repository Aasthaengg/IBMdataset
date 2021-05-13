n=int(input())
s=list(input())
w=s.count("W")
e=s.count("E")
x=[0 for i in range(n)]
for i in range(1,n):
    if s[i-1]=="W":
        x[i]=x[i-1]+1
    else:
        x[i]=x[i-1]
ans=n
for i in range(n):
    z=2*x[i]+e-i
    if s[i]=="E":
        z-=1
    ans=min(ans,z)
print(ans)
