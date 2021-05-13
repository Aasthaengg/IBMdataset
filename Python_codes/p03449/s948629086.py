n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]

ans = 0
res = 0
for i in range(n):
   sum_a1 = sum(a[0][0:i + 1])
   sum_a2 = sum(a[1][i:n])
   res = max(res, sum_a1 + sum_a2)
print(res)