S = list(input())
for i in range(len(S)):
  if S[0] == "K":
    S.insert(0,"A")
for i in range(len(S)):
  if S[i] == "H" and S[i+1] != "A":
    S.insert(i+1,"A")
for i in range(len(S)):
  if S[i] == "B" and S[i+1] != "A":
    S.insert(i+1,"A")
for i in range(len(S)):
  if S[-1] == "R":
    S.append("A")

if "".join(S) == "AKIHABARA":
  print("YES")
else:
  print("NO")
