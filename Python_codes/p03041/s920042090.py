N, K = map(int, input().split())
S = input()
ans = ""
for i in range(N):
  if i == K-1:
    ans += chr(ord(S[i])+32)
  else:
    ans += S[i]
print(ans)