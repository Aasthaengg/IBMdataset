S = input()
N = len(S)
ans = 0
cnt = 0
i = 0
while i < N:
  if S[i] == "A":
    cnt += 1
    i += 1
  elif "".join(S[i:i+2]) == "BC":
    ans += cnt
    i += 2
  else:
    cnt = 0
    i += 1
print(ans)