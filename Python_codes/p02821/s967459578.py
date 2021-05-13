import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
rev_A = A[::-1]

def check(x, a=A, m=M):
  result = False
  n = len(a)
  count = 0
  for ai in a:
    count += (n - bisect.bisect_left(a, x-ai))
  
  return count>=m


left = 0
right = 2*10**5 + 1
mid = (left + right) // 2
while right - left > 1:
  if check(mid):
    left = mid
  else:
    right = mid
    
  mid = (left + right)//2

x = left
if check(right):
  x = right

accum_A = [rev_A[0]]
for i, a in enumerate(rev_A):
  if i == 0:
    continue
  accum_A.append(accum_A[-1] + a)

ans = 0
count = 0
surplus = 2*10**5
for ai in rev_A:
  idx = bisect.bisect_left(A, x-ai)
  if idx == N:
    break
  ans += (N-idx)*ai + accum_A[N-idx-1]
  count += N - idx
  surplus = min(surplus, ai+A[idx])


print(ans - (count-M)*surplus)