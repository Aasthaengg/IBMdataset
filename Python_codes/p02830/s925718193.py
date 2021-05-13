# 148b

from sys import stdin

N = int(stdin.readline().strip())
S, T = stdin.readline().strip().split(" ")

for s,t in zip(S,T):
  print(s+t,end="")
