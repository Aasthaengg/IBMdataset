n = int(input())
a = list(map(int , input().split()))
count = 0
for i in range(n):
  if a[i] == 0:
    continue
  if a[a[i] - 1] == i + 1:
    a[a[i] - 1] = 0
    count += 1
print(count)