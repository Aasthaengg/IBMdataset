S = input()
w = int(input())
ans = ""
i = 0
while i < len(S):
  ans += S[i]
  i += w
print(ans)