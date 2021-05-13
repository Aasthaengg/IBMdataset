import sys
from itertools import accumulate

readline=sys.stdin.readline
read=sys.stdin.read

def main():
  q,*lr=map(int,read().split())
  n=10**5
  ansl=[]
  sieve=[1]*(n+1)
  sieve[0],sieve[1]=0,0
  for i in range(2,n):
    if sieve[i]:
      sieve[2*i::i]=[0 for _ in range(2*i,n+1,i)]
  ans=[0]*(n+1)
  for i in range(3,n):
    if sieve[i]==1 and sieve[(i+1)//2]==1:
      #ans[i]=1
      ans[i]=ans[i-1]+1
    else:
      ans[i]=ans[i-1]
  
  #ans=list(accumulate(ans))
  for l,r in zip(*[iter(lr)]*2):
    print(ans[r]-ans[l-1])

if __name__=='__main__':
  main()
