k, x = map(int, input().split())

a = []
for i in range(k):
  a.append(x-i)
for i in range(k-1):
  a.append(x+1+i)
a.sort()
res = ''
for i in range(len(a)):
  res += str(a[i])
  if i != len(a)-1:
    res += (' ')
  
print(res)