S = str(input())
A = "dream"
B = "dreamer"
C = "erase"
D = "eraser"
while len(S) >= 5:
  if len(S) >= 7 and S[-7:] == B:
    S = S[:-7]
  elif len(S) >=6 and S[-6:] == D:
    S = S[:-6]
  elif S[-5:] == A or S[-5:] == C:
      S = S[:-5]
  else:
    break
if len(S) == 0:
  print("YES")
else:
  print("NO")