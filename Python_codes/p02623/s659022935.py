'''
Created on 2020/08/31

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  N,M,K=map(int,pin().split())
  A=list(map(int,pin().split()))
  B=list(map(int,pin().split()))
  a=[0]
  b=[0]
  for i in range(N):
    a.append(a[i]+A[i])
  for j in range(M):
    b.append(b[j]+B[j])
  ans=0
  l=M
  for k in range(N+1):
    if a[k]>K:
      break
    while b[l]>K-a[k]:
      l-=1
    ans=max(ans,l+k)
  print(ans)
  return
main()
#解説AC