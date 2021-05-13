N=int(input())
S,T=input().split()
ans=""
for x in range(N):
  ans += S[x]+T[x]
print(ans)
