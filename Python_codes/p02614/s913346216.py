'''
Created on 2020/08/30

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  H,W,K=map(int,pin().split())
  C=[pin()[:-1] for _ in [0]*H]
  ans=0
  for i in range(2**H):
    for j in range(2**W):
      black=0
      for k in range(H):
        for l in range(W):
          if (i>>k)&1==0 and (j>>l)&1==0 and C[k][l]=="#":
            black+=1
      if black==K:
        ans+=1
  print(ans)
  return
main()
#解説AC
