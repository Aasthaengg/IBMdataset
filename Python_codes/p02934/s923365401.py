n = int(input())
lst = list(map(int, input().split()))
res = 0
for i in range(n):
  res += (1 / lst[i])
print(1 / res)