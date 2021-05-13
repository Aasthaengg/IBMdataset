'''
Created on 2020/09/08

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  X,Y,Z,K=map(int,pin().split())
  A=list(map(int,pin().split()))
  B=list(map(int,pin().split()))
  C=list(map(int,pin().split()))
#   A.sort(reverse=True)
#   B.sort(reverse=True)
#   C.sort(reverse=True)

  d=[]
  for i in A:
    for j in B:
      d.append(i+j)
  d.sort(reverse=True)
  d=d[:K]
  ans=[]
  for k in d:
    for l in C:
      ans.append(k+l)
  ans.sort(reverse=True)
  for m in range(K):
    print(ans[m])
  return
main()

