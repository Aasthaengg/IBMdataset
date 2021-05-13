H,W,A,B = map(int, input().split())

if A == 0 and B == 0:
  for _ in range(H):
    print("".join("0" * W))
  exit(0)
  
ANS = []
cnt = B
roll = 0
for i in range(B):
  wk = ["1"] * A + ["0"] * (W-A)
  ANS.append(wk)
for i in range(H-B):
  wk = ["0"] * A + ["1"] * (W-A)
  ANS.append(wk)
  
for ans in ANS:
  print("".join(ans))

