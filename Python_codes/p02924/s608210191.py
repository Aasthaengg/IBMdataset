import math
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**8)
INF = float('inf')
MOD = 10**9+7


def main():
  N = int(input())
  ans = 0
  if N==1:
    ans = 0
  else:
    ans = (N-1) * N//2
  print(ans)
  
if __name__ == '__main__':
  main()