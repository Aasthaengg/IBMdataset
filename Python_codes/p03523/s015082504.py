S = list(input())
if S[0] != "A":
  S.insert(0,"A")
if len(S) < 5:
  print("NO")
  exit()
if S[4] != "A":
  S.insert(4,"A")
if len(S) < 7:
  print("NO")
  exit()
if S[6] != "A":
  S.insert(6,"A")
if len(S) < 5:
  print("NO")
  exit()
if len(S) < 8:
  print("NO")
  exit()
if S[-1] != "A":
  S.append("A")
s = ""
for i in S:
  s += i
print("YES" if s == "AKIHABARA" else "NO")