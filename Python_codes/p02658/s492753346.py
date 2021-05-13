n = int(input())
a = list(map(int,input().split()))
sum = 1

for i in range(n):
  if a[i] == 0:
    sum = 0

for i in range(n):
  sum = sum*a[i]
  if sum >10**18:
    sum = -1
    break

print(sum)