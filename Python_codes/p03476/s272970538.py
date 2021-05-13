q=int(input())
lr=[tuple(map(int,input().split())) for _ in range(q)]

def main():
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
      ans[i]=ans[i-1]+1
    else:
      ans[i]=ans[i-1]

  for e in lr:
    print(ans[e[1]]-ans[e[0]-1])

if __name__=='__main__':
  main()