S = input()
n = len(S)
w = int(input())
i = 0
ans = S[0]
while i + w < n:
  i += w
  ans += S[i]
print(ans)