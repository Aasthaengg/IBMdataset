from bisect import bisect_left

N, M=map(int, input().split())
A=list(map(int, input().split()))

A.sort()
left=0
right=max(A) * 2 + 1

while left+1<right:
  mid=(left + right) // 2
  
  cnt=0
  for i in range(N):
    cnt+=N - bisect_left(A, mid - A[i])
  if cnt>=M:
    left=mid
  else:
    right=mid

mon=[0]
for a in A:
  mon.append(mon[-1] + a)

ans=0
cnt=0
for i in range(N):
  bi = bisect_left(A, left - A[i])
  ans+=(mon[-1] - mon[bi]) + (N - bi) * A[i]
  cnt+=(N - bi)
ans-=(cnt - M) * left

print(ans)