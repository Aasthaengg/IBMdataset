a = int(input())
count = 0
lst = []
while a > 0:
  lst.append(a%10)
  a //= 10
lst.reverse()
for i in lst:
  if i == 2:
    count = count + 1
print(count)