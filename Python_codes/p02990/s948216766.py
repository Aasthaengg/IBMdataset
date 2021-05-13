def nCk(_n,_k):
  return fact[_n]*ifact[_k]*ifact[_n-_k]%m

def main():
  for i in range(1,2001):
    fact[i]=fact[i-1]*i
    ifact[i]=pow(fact[i],m-2,m)
  n,k=map(int,input().split())
  for i in range(1,k+1):
    print(nCk(n-k+1,i)*nCk(k-1,i-1)%m if n-k>=i-1 else 0)

if __name__=='__main__':
  fact,ifact,m=[1]*2005,[1]*2005,10**9+7
  main()