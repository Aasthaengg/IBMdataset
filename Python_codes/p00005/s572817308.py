while True:
  try:
    a,b=map(int,input().split())
    if a<b:
      a,b=b,a
    s=b
    r=a%s
    while True:
      if r==0:
        G=s
        break
      else:
        s,r=r,s%r
    L=int((a*b)/G)
    print(G,L)
  except EOFError:
    break
