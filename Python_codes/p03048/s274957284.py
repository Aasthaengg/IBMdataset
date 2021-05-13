#!/usr/bin/env python3

def solve(r,b,g,n):
  r_max = n // r
  b_max = n // b
  g_max = n // g
  ans = 0
  for i in range(r_max+1):
    for j in range(b_max+1):
      rest = n - (r*i + b*j)
      if rest >= 0 and rest % g == 0:
        ans += 1
  return ans



def main():
  R,G,B,N = map(int,input().split())
  print(solve(R,G,B,N))
  return

if __name__ == '__main__':
  main()
