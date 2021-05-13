N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

helper = []
need, ans = 0, 0

if sum(A) < sum(B):
  print(-1)
  exit()

for i in range(N):
  if A[i] > B[i]:
    helper.append(A[i] - B[i])
  elif A[i] < B[i]:
    need += B[i] - A[i]
    ans += 1

helper = sorted(helper, reverse=True)
i = 0
while need > 0:
  need -= helper[i]
  i += 1
  ans += 1
print(ans)