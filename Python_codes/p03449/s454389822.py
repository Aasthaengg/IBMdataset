n = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
res = 0
for i in range(n):
  res = max(res, sum(lst1[:i + 1]) + sum(lst2[i:]))
print(res)