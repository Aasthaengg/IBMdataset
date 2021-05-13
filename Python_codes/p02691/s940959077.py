def main():
  ## IMPORT MODULE
  #import sys

  #sys.setrecursionlimit(100000)
  #input=lambda :sys.stdin.readline().rstrip()
  from collections import defaultdict

  #f_inf=float("inf")
  #MOD=10**9+7
  
  if 'get_ipython' in globals(): 
    ## SAMPLE INPUT
    n = 6
    A = [2, 3, 3, 1, 3, 1]

  else:
    ##INPUT 
    n = int(input())
    A = list(map(int, input().split()))

  ## SUBMITION CODES HERE
  d = defaultdict(int)
  ans = 0
  for j in range(n):
    Dif = j - A[j]
    ans += d[Dif]
    Sum = A[j] + j
    d[Sum] += 1
  print(ans)
  
main()