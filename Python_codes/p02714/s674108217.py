import collections as cl
N = int(input())
S = input()
a,b = '',''
d = cl.Counter(S)
rgb = d['R']*d['B']*d['G']
expt = 0
for i in range(N):
  a = S[i]
  for j in range(i,(N+i-1)//2+1):
    if S[j] != a:
      b = S[j]
      k = 2*j-i
      if S[k]!=b and S[k]!=a:
        expt += 1
print(rgb-expt)