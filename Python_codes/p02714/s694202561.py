N = int(input())
S = input()
a,b = '',''
r = S.count('R')
g = S.count('G')
b = len(S)-r-g
rgb = r*g*b
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