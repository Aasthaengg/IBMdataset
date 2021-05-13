import numpy as np
def main():
  N = int(input())
  K = int(input())
  x = list(map(int, input().split()))
  ans = 0
  for i in x:
    ans += 2*min(i, K-i)
  print(ans)
if __name__ == "__main__":
  main()