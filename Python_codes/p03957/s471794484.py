S=input()
N=len(S)

if "C" in S and "F" in S:
  c=S.index("C")
  S=S[::-1]
  f=N-S.index("F")-1
  #print(c,f)
  print("Yes" if c<f else "No")
else: 
  print("No")