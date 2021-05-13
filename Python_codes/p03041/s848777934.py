import sys
a=sys.stdin.readline()
res = [int(i) for i in a.split() if i.isdigit()] 
N,K = [res[i] for i in (0,1)]
S=sys.stdin.readline(N)
K-=1
if N<0 or N>50:
  print("Error")
else:
  x=S[:K]
  y=S[K].lower()
  z=S[K+1:]
  print(x+y+z)