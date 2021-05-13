N = int(input())
A = list(map(int, input().split()))
a = 0
for i in range(N):
  if A[i]%2==1:
    a += 1
ans = 'NO'
if a%2==0:
  ans = 'YES'
print(ans)