N,X = map(int, input().split())
S = []
for _ in range(N):
    S.append(int(input()))
list = sorted(S)
K = list[0]
H = sum(list)
ans = N
if K <= X-H:
  ans=N+(X-H)//K
print(ans)