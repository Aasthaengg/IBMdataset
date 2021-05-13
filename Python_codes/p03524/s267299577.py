from collections import Counter

S = input()
d = Counter(S).values()
if len(S) == 1:
  ans = "YES"
elif len(S) == 2:
  if S[0] != S[1]:
    ans = "YES"
  else:
    ans = "NO"
elif len(d) == 3 and max(d) - min(d) <=1:
  ans = "YES"
else:
  ans = "NO"
print(ans)
