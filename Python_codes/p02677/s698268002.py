import math
from sys import stdin
input = stdin.readline


def main():
  A, B, H, M = list(map(int, input().split()))

  theta_a = 2*math.pi * ((H * 60 + M) / (12*60))
  theta_b = 2*math.pi * (M / 60)

  print( math.sqrt( (A*math.cos(theta_a) - B*math.cos(theta_b))**2 + \
                    (A*math.sin(theta_a) - B*math.sin(theta_b))**2 ) )

if(__name__ == '__main__'):
  main()
