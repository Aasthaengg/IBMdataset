#!/usr/bin/python3
# -*- coding: utf-8 -*-


def get_fact(N):
  ret = set([N])
  for i in range(2,int(N**0.5)+2):
    if N%i == 0:
      ret.add(i)
      ret.add(N//i)
  return ret


def main():
  ## input
  N,K = map(int, input().split())
  An = list(map(int, input().split()))

  ## Solve
  fset = get_fact(sum(An))
  ans = 1
  for f in fset:
    Amod = [a%f for a in An]
    Amod = sorted(Amod)
    for i in range(len(Amod)):
      if sum(Amod[:i])==f*(N-i)-sum(Amod[i:]) and sum(Amod[:i])<=K:
        ans = max(ans,f)
  return ans


if __name__ == "__main__":
  ans = main()
  print(ans)
