N,M,C = map(int,input().split())
B = list(map(int,input().split()))
num = C
ans = 0
for i in range(N):
  l = list(map(int,input().split()))
  for j in range(M):
    num += B[j] * l[j]
  if num > 0:
    ans += 1
    num = C
  else:
    num = C
print(ans)