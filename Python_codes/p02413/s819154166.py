r,c = map(int,input().split())
a =[]

for i in range(r) :
  a.append(list(map(int,input().split())))
  a[i].append(sum(a[i]))

b = list(map(sum,zip(*a)))

for i in range(r) :
  print(*a[i])
print(*b)
