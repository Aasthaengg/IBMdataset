#!/usr/bin/env python3
from collections import Counter


def combi(n):
  return n*(n-1)//2

def solve(n,a):
  d = Counter(a)
  patterns = dict((k,combi(v)) for k,v in d.items())
  patterns_sum = sum(patterns.values())
  ans = [0]*n
  for i in range(n):
    ans[i] = patterns_sum - patterns[a[i]] + combi(d[a[i]]-1)
  return ans



def main():
  N = int(input())
  a = list(map(int,input().split()))
  ans = solve(N,a)
  for i in range(len(ans)):
    print(ans[i])
  return

if __name__ == '__main__':
  main()
