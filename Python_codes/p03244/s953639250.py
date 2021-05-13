from collections import *
N = int(input())
V = list(map(int,input().split()))
E = Counter(V[0::2]).most_common()+[(0,0)]
O = Counter(V[1::2]).most_common()+[(0,0)]

if E[0][0]!=O[0][0]:
  print(N-E[0][1]-O[0][1])
else:
  print(N-max(E[0][1]+O[1][1],E[1][1]+O[0][1]))