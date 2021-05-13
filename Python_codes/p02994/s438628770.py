n,l=map(int, input().split())
a=[l+i for i in range(n)]
value1=1000
value=0
for i in range(n):
  if abs(a[i])<value1:
    value1=abs(a[i])
    value2=a[i]
print(sum(a)-value2)