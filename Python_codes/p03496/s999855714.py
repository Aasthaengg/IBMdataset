n = int(input())
a = list(map(int, input().split()))

j = -1
m = -1
for i in range(n):
  t = abs(a[i])
  if t > m:
    j = i
    m = t
print(2*(n-1))
for i in range(n):
  if i == j:
    continue
  print(str(j+1)+" "+str(i+1))

if a[j]>0:
  for i in range(n-1):
    print(str(i+1)+" "+str(i+1+1))
else:
  for i in range(n-1):
    print(str(n-1-i+1)+" "+str(n-1-(i+1)+1))
