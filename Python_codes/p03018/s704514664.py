import sys
input = sys.stdin.readline
S = list(input())[: -1]
t = []
res = 0
i = 1
while i < len(S):
  if S[i - 1] == "B" and (S[i] == "C"):
    t.append("X")
    i += 1
  else:
    if S[i - 1] == "A": t.append(S[i - 1])
    else: t.append("Y")
  i += 1
tt = "".join(t).split("Y")
for x in tt:
  xs = x.count("X")
  for i in range(len(x)):
    if x[i] == "A":
      res += xs
    else: xs -= 1
print(res)