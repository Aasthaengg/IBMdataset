l,r=[int(x) for x in input().split()]
L=l%2019
a=2020
for i in range(1,2020):
  if l+i<=r:
    for j in range(i):
      a=min((L+j)*(L+i)%2019,a)
print(a)