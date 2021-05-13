N = int(input())
A = list(map(int, input().split(' ')))
ans = 0
gap = 0
for i in range(1,N):
  if ( A[i-1] + gap ) > A[i]:
    gap = ( A[i-1] + gap ) - A[i]
  else:
    gap = 0
  ans += gap
    
print(ans)