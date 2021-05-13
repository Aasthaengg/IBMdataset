n = int(input())
lst = list(map(int, input().split()))
res = 0
temp = 0
for i in range(1, n):
  if lst[i] <= lst[i - 1]:
    temp += 1
    res = max(res, temp)
  else:
    temp = 0
print(res)