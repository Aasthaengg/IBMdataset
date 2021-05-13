#!/usr/bin/env python3

def solve(n,y):
  billUnit = (10000,5000,1000)
  for i in range(0,y//billUnit[0]+1):
    for j in range(0,y//billUnit[1]+1):
      rest = y - billUnit[0] * i - billUnit[1] * j
      k = n - i - j
      if billUnit[2] * k == rest and k >= 0:
        return i,j,k
  return -1,-1,-1



def main():
  N,Y = map(int,input().split())
  print(*solve(N,Y))
  return

if __name__ == '__main__':
  main()
