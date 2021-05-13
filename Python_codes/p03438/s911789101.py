def check():
  N = int(input())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  diff = sum(B)-sum(A)
  if diff < 0:
    return 'No'
  cnt = 0
  for i in range(N):
    cnt += max((B[i]-A[i]+1)//2,0)
  if diff < cnt:
    return 'No'
  return 'Yes'
print(check())