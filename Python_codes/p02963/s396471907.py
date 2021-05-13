S = int(input())
p = S%(10**9)
k = (S-p)//10**9
L = [0,0,10**9,1,10**9-p,(k+1)]
if S != 10**18:
  print(" ".join(map(str,L)))
else:
  L = [0,0,10**9,0,0,10**9]
  print(" ".join(map(str,L)))