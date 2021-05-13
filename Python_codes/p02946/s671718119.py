k, x = map(int, input().split())
li = []
for i in range(1, k):
  li.append(x + i)
  li.append(x - i)
li.append(x)  
a = sorted(li)
print(*a)