n = int(input())
A = list(map(int,input().split()))
cnt = 0
for i in range(n):
  if A[i] % 2 == 1:
    cnt += 1
ans = 3**n - 2**(n-cnt)
print(ans)