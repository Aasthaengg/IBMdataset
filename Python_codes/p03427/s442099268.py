N=input()
l=len(N)-1
h=int(N[0])
N=int(N)
if N==(h+1)*10**l-1:
  print(h+9*l)
else:
  print(h+9*l-1)