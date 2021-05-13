n=int(input())
m=10**9+7

a=[1,4,16]
g=[1,4,15]
c=[1,4,14]
t=[1,4,16]

for i in range(3,n):
  a.append((a[i-1]+g[i-1]+c[i-1]+t[i-1])%m)
  t.append((a[i-1]+g[i-1]+c[i-1]+t[i-1])%m)
  g.append((a[i-1]+g[i-1]+(c[i-1]-a[i-2]+g[i-3])+t[i-1])%m)
  c.append(((a[i-1]-g[i-2])+(g[i-1]-a[i-2]-2*a[i-3])+c[i-1]+(t[i-1]-a[i-3]))%m)

n=n-1

ans=a[n]+g[n]+c[n]+t[n]
print(ans%m)
