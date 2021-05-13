import sys
sys.setrecursionlimit(100000)

def solve(x,a,ans=0):
  if x == 0:
    return ans
  else:
    return solve(x-1,a[1:],ans+1/a[0])
  
N = int(input())
a = list(map(int,input().split()))

print(1/solve(N,a))