a,b,c,d,e,k=[int(input()) for i in range(6)]
if b-a>k or c-a>k or d-a>k or e-a>k or c-b>k or d-b>k or e-b>k or d-c>k or e-c>k or e-d>k:
  print(":(")
else:
  print("Yay!")