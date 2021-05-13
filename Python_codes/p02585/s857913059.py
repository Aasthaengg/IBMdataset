n,k=map(int,input().split())
P=list(map(int,input().split()))
P=[p-1 for p in P]
C=list(map(int,input().split()))

def main():
  ans=-float('inf')
  for si in range(n):
    x=si
    S=[]
    tot=0
    while True:
      x=P[x]
      S.append(C[x])
      tot+=C[x]
      if x==si:
        break
    l=len(S)
    t=0
    for i in range(l):
      t+=S[i]
      if i+1>k:
        break
      now=t
      if tot>0:
        e=(k-i-1)//l
        now+=tot*e
      ans=max(ans,now)
  return ans      


if __name__=='__main__':
  print(main())
