n = int(input())
lst = list(map(int, input().split()))
lst = [lst[0]] + lst + [lst[-1]]
res = 0
for i in range(n):
  res += min(lst[i + 1], lst[i])
print(res)