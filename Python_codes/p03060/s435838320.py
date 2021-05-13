import numpy as np
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**8)
INF = float('inf')
MOD = 10**9+7


def main():
  N = int(readline())
  V = np.array(readline().split(), np.int64)
  C = np.array(readline().split(), np.int64)
  D = V-C
  E = np.where(D<0,0,D)
  print(E.sum())
  
  
  
  
if __name__ == '__main__':
  main()