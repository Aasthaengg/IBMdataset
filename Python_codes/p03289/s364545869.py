S = list(input())
ans = "AC"

if S[0] != "A":
  ans = "WA"

if S[2:-1].count("C") != 1:
  ans = "WA"
else:
  S.pop(S[2:-1].index("C") + 2)

if not "".join(S[1:]).islower():
  ans = "WA"

print(ans)
