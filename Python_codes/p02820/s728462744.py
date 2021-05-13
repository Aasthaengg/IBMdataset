from itertools import groupby
N, K = map(int, input().split())
R, S, P = map(int, input().split())
D = {"r":P, "s":R, "p":S}
T = list(input())
c = 0
for i in range(K):
  gr = groupby(T[i::K])  
  for key, group in gr:
    l = len(list(group))
    d = D[key]
    c += d*((l+1)//2)
print(c)