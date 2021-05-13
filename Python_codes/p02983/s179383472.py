L,R=map(int,input().split())
m=10**4
a=min(R,L+2019)

for i in range(L,a):
  for j in range(i+1,a+1):
    m=min(i*j%2019,m)
print(m)