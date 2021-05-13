n = int(input())
a = list(map(int,input().split()))

count = 0
temp = a[0]

for i in range(n):
  if a[i] >= temp:
    temp = a[i]
  else:
    count += temp - a[i]
print(count)