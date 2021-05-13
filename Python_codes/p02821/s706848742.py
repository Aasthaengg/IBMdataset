import bisect


N, M = map(int, input().split())
Al = list(map(int, input().split()))
Al.sort() # 左手で握手する人のリスト
Ar = Al.copy()[::-1] # 右手で握手する人のリスト

def count_large_2(L1, L2, x):
  # L1.sort()
  # L2.sort(reverse=True)
  N1, N2 = len(L1), len(L2)
  i = j = 0
  c = 0
  while i<N1 and j<N2:
    if L1[i]+L2[j] >= x:
      c += 1
      j += 1
      if j >= N2:
        c += (N1-i-1) * N2
    else:
      i += 1
      if i>=N1:
        continue
      c += j
  return c

left = 0 # True
right = Al[-1]*2 + 1 # False
while left+1 < right:
  mid = (left + right) // 2
  if count_large_2(Al, Ar, mid) >= M:
    left = mid
  else:
    right = mid


x = left
accum_A = [Ar[0]]
for i, a in enumerate(Ar):
  if i == 0:
    continue
  accum_A.append(accum_A[-1] + a)


ans = 0
count = 0
surplus = 2*10**5
for ai in Ar:
  idx = bisect.bisect_left(Al, x-ai)
  if idx == N:
    break
  ans += (N-idx)*ai + accum_A[N-idx-1]
  count += N - idx
  surplus = min(surplus, ai+Al[idx])
 
 
print(ans - (count-M)*surplus)