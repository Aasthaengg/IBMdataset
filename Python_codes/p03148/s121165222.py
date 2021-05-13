import sys
input = sys.stdin.readline

def main():
  N, K=map(int,input().split())
  sushies=[list(map(int,input().split())) for i in range(N)]
  sushies.sort(reverse=True, key=lambda x:x[1])
  dsum=0
  tset=set()
  kubi=[]
  for i in range(K):
    dsum+=sushies[i][1]
    t=sushies[i][0]
    if t in tset:
      kubi.append(sushies[i])
    tset.add(t)
  x=len(tset)
  koho=[]
  for i in range(K,N):
    t=sushies[i][0]
    if not(t in tset):
      koho.append(sushies[i])
      tset.add(t)
  ind=0
  ans=dsum+x*x
  while(ind < len(kubi) and ind < len(koho)):
    dsum=dsum-kubi[-1-ind][1]+koho[ind][1]
    x+=1
    ans=max(ans, dsum+x*x)
    ind+=1
  print(ans)
  
if __name__=="__main__":
  main()