#!/usr/bin/env python3



def rateToColor(rate):
  if 0 < rate < 400:
    return 0
  elif rate < 800:
    return 1
  elif rate < 1200:
    return 2
  elif rate < 1600:
    return 3
  elif rate < 2000:
    return 4
  elif rate < 2400:
    return 5
  elif rate < 2800:
    return 6
  elif rate < 3200:
    return 7
  else:
    return 8


def solve(n,a):
  flags = [False]*8
  numOfRainbow = 0
  for rate in a:
    color = rateToColor(rate)
    if color != 8:
      flags[color] = True
    else:
      numOfRainbow += 1
  if sum(flags):
    return sum(flags), sum(flags)+numOfRainbow
  else:
    return 1,numOfRainbow


def main():
  N = int(input())
  a = list(map(int,input().split()))
  print(*solve(N,a))
  return

if __name__ == '__main__':
  main()
