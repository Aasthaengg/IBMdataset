K, T = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
other = sum(A)-max(A)
if max(A)-1>other:
  ans = max(A)-1-other

print(ans)