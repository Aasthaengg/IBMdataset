n = int(input())
b = list( map(int,input().split()) )

a = [0] * n
c = b[0]
a[0] = b[0]
for i,data in enumerate(b):
  if b[i] >= c:
    a[i+1] = b[i]
  else :
    a[i],a[i+1] = b[i],b[i]
  c = b[i]

print(sum(a))
