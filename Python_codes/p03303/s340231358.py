S = str(input())
w = int(input())
idx = 0
ans = ""
while idx < len(S):
  ans += S[idx]
  idx += w
print(ans)