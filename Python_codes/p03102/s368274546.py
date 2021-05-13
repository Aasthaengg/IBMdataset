n,m,c = map(int,input().split(" "))
b = list(map(int,input().split(" ")))

count = 0
for i in range(n):
  li = [c]
  a = list(map(int,input().split(" ")))
  for x, y in zip(a,b):
    li.append(x*y)
  li_sum = sum(li)
  if li_sum > 0:
    count += 1
print(count)