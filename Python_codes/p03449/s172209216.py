n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

res = 0
for i in range(n):
  a1_sum = sum(a1[:i+1])
  a2_sum = sum(a2[i:])
  res = max(res, a1_sum + a2_sum)

print(res)