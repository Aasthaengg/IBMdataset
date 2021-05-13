N,K=[int(i) for i in input().split()]
R={}
for n in range(N):
    a,b=[int(i) for i in input().split()]
    R[a]=b+(R[a] if (a in R) else 0)
RR=sorted(list(R.keys()))
k=0
for ir in range(len(RR)):
    k+=R[RR[ir]]
    if k>=K:
      print(RR[ir])
      break
  
  
