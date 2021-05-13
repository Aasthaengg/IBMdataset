n=int(input())
m=10**15+1
mi=0
for i in range(5):
  a=int(input())
  if a<m:
    m=a
    mi=i
print((n-1)//m+1+5-1)