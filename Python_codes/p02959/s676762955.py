N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 0

for n in range(N):
  if B[n]<=A[n]:
    ans+=B[n]
  elif B[n]<=A[n]+A[n+1]:
    ans+=B[n]
    A[n+1]-=B[n]-A[n]
  else:
    ans+=A[n]+A[n+1]
    A[n+1] = 0

print(ans)