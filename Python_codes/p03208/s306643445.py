n, k = map(int, input().split())
lst = []
for i in range(n):
  lst.append(int(input()))
lst.sort()
res = 10 ** 9
for i in range(n - k + 1):
  temp = lst[i + k - 1] - lst[i]
  if temp < res:
    res = temp
print(res)