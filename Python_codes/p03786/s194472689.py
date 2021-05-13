N = int(input())
A = list(map(int,input().split()))
A.sort()
ans = 1
now = A[0]
for i in range(1,N):
  if A[i] > 2*now:
    ans = 1
    now += A[i]
  else:
    ans += 1
    now += A[i]
print(ans)
