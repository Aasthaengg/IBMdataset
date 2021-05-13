n = int(input())
lst = list(map(int, input().split())) + [0]
cnt = 1
res = 0
for i in range(n):
  if lst[i + 1] == lst[i]:
    cnt += 1
  else:
    res += (cnt // 2)
    cnt = 1
print(res)