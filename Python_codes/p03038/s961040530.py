n, m = map(int, input().split())
a = [int(i) for i in input().split()]
a = sorted(a)

l = []
for i in range(m):
  l.append(list(map(int, input().split())))
  
l = sorted(l, reverse=True, key=lambda x: x[1])

b = []
for _ in range(n):
  b.append(l[0][1])
  l[0][0] -= 1
  if l[0][0] == 0:
    l.pop(0)
  if l == []:
    break

for i in range(len(b)):
  if a[i] < b[i]:
    a[i] = b[i]
  else:
    break
    
print(sum(a))
