n = int(input())

a = [0 for i in range(n)]

count = 0

for i in range(n):
  if (i+1)%3 == 0 or (i+1)%5 == 0:
    continue
  else:
    a[i] = (i+1)
    count += (i+1)

print(count)