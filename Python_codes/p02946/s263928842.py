k,x = map(int,input().split())
li = []
i = 0
while i in range (k):
  li.append(x-i)
  li.append(x+i)
  i += 1
a = sorted(set(li))
print(*a)