N = int(input())
D,X = map(int,input().split())
cnt = 0
for _ in range(N):
  A = int(input())
  for j in range (D):
    if A*j + 1 <= D:
      cnt += 1
    else:
      break
print(X+cnt)