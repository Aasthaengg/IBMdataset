n,a,b=map(int,input().split())
u=sorted(list(map(int,input().split())))[::-1]
v=sum(u[:a])/a
print(v)
f=[1]
for i in range(50):f+=[f[-1]*(i+1)]
x=u.count(u[a-1])
if u[0]==u[a-1]:print(sum(f[x]//(f[x-i]*f[i])for i in range(a,b+1)))
else:y=u[:a].count(u[a-1]);print(f[x]//(f[x-y]*f[y]))