H, N = map(int, input().split())
A = list(map(int, input().split()))
ans = "No"
sum_ = sum(A)
if H <= sum_:
  ans = "Yes"
print(ans)
