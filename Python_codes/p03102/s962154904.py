N, M, C = map(int, input().split())
B = list(map(int, input().split()))
ans = 0
for i in range(N):
  A = list(map(int, input().split()))
  tmp = 0
  for i,j in zip(B,A):
    tmp += i*j
  if tmp + C > 0:
    ans += 1
print(ans)
