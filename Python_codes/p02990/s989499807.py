import sys
input = sys.stdin.readline
def main():
  n,k=map(int,input().split())
  mod=pow(10,9)+7
  ans=0
  def ncr_mod(n,r,mod):
    a,b=1,1
    for i in range(r):
      a*=n-i
      a%=mod
      b*=i+1
      b%=mod
    return (a*pow(b,mod-2,mod))%mod
  for i in range(1,k+1):
    a=ncr_mod(n-k+1,i,mod)
    b=ncr_mod(k-1,i-1,mod)
    print((a*b)%mod)
if __name__=='__main__':
  main()
