N = int(input())
a = list()
count = 0
value = 0
for i in range(N):
  a.append(int(input()))

for i in range(N):
  if a[value] == 2:
    print(count + 1)
    break
  elif a[value] == 0:
    print(-1)
    break
  else:
    tmp = a[value] - 1
    a[value] = 0
    value = tmp
    count += 1