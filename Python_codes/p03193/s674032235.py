n,h,w = (int(i) for i in input().split())
a = []
b = []
for i in range(n):
  a0,b0 = (int(i) for i in input().split())
  a.append(a0)
  b.append(b0)

count = 0
for i in range(n):
  if a[i]>=h and b[i]>=w:
  	count+=1
print(count)