import sys
sys.setrecursionlimit(10000)

N = int(input())
l=[-1]*(N+1)

def lyuka(x):
  if l[x] != -1:
    return l[x]
  if x == 0:
    return 2
  if x == 1:
    return 1
  lyu = lyuka(x-1) + lyuka(x-2)
  l[x] = lyu
  return lyu

print(lyuka(N))