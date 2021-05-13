#!/usr/bin/env python3

# input = stdin.readline



def main():
  N = int(input())
  p = list(map(int,input().split()))
  def solve(n,p):
    assert n >= 2
    target = sum(0 if p[i]==i+1 else 1 for i in range(n)) 
    return target == 0 or target == 2
  print("YES" if solve(N,p) else "NO")
  return

if __name__ == '__main__':
  main()
