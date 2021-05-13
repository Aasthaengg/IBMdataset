f=lambda:map(int,input().split())
n,T=f()
m=1001
for _ in range(n):
  c,t=f()
  if t<=T: m=min(m,c)
print([m,'TLE'][m>1000])