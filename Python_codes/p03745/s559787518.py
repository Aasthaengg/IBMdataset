N = int(input())
A = list(map(int, input().split()))

i = 0
ans = 0
for a in A:
  right, right2 = i, i
  while right+1 < N and A[right] <= A[right+1]: right += 1
  while right2+1 < N and A[right2] >= A[right2+1]: right2 += 1
  i = max(right, right2) + 1
  ans += 1
  if i >= N: break
print(ans)