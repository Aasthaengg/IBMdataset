S = str(input())
win = 0
for s in S:
  if s == "o":
    win += 1
if (win + (15 - len(S))) >= 8:
  print("YES")
else:
  print("NO")