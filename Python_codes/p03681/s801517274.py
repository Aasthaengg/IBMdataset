def main():
  p=10**9+7
  def modpfac(n):
    ret=1
    for i in range(1,n+1):
      ret=ret*i % p
    return ret
  n,m=map(int,input().split())
  if abs(m-n)>1:
    return print(0)
  elif abs(m-n)==1:
    return print(modpfac(n)*modpfac(m)%p)
  else:
    return print(2*modpfac(n)*modpfac(m)%p)
 
main()