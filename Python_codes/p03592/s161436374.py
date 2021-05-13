N,M,K=map(int,input().split())
cond=False
for i in range(N+1):
  for j in range(M+1):
    b=i*(M-j)+j*(N-i)
    if b==K:
      cond=True
      break
  if cond:
    break
print("Yes" if cond else "No")
