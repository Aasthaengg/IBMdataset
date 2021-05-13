N=int(input())
W=[]
W.append(N)
i=1
while True:
  if N%2==0:
    N=N/2
    i+=1
    if N in W:
      print(i)
      exit()
    else:
      W.append(N)
  else:
    N=3*N+1
    i+=1
    if N in W:
      print(i)
      exit()
    else:
      W.append(N)