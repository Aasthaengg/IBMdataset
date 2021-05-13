n=int(input())
S,T=map(str,input().split())
ans = ""
for i in range(n):
  ans += S[i]
  ans += T[i]
print(ans)