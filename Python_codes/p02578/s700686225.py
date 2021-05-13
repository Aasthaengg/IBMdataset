N = int(input())
A = [int(i) for i in input().split()]
pre_a = A[0]
ans = 0

for a in A[1:]:
  ans += max(0, pre_a - a)
  pre_a = max(pre_a, a)

print(ans)