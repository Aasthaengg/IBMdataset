from itertools import *
N = int(input())
D = {"M":0,"A":0,"R":0,"C":0,"H":0}

for n in range(N):
  s = input()
  if s[0] in "MARCH":
    D[s[0]]+=1

print(sum(a*b*c for a,b,c in combinations(D.values(),3)))