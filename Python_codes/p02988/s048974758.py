n = int(input())
lst = list(map(int, input().split()))
res = 0
for i in range(1, n - 1):
  if lst[i] == sorted([lst[i - 1], lst[i], lst[i + 1]])[1]:
    res += 1
print(res)