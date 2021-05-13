#!/usr/bin/env python3

def solve(n,v,c):
  l = [v[i] -c[i] for i in range(n)]
  l = filter(lambda x: x >=0,l)
  return sum(l)



def main():
  N = int(input())
  V = list(map(int,input().split()))
  C = list(map(int,input().split()))
  print(solve(N,V,C))
  return

if __name__ == '__main__':
  main()
