from bisect import bisect_left
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(A)
p = 10**9+7

list1 = [bisect_left(B,A[i]) for i in range(N)]
list2 = [bisect_left(sorted(A[i+1:]),A[i]) for i in range(N)]
ans = 0
for i in range(N):
  ans += list2[i] * K
  ans %= p
  tmp = K * (K-1) // 2
  ans += list1[i] * tmp
  ans %= p
print(ans)