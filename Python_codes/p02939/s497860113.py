S = input()

s = S[0]
cnt = 1
t = ""
for i in range(1, len(S)):
  t += S[i]
  if t != s:
    cnt += 1
    s = t
    t = ""

print(cnt)