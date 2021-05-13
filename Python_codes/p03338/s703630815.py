N = int(input())
S = list(input())

for i in range(N):
  ans = 0
  for j in range(N):
    f = {}
    b = {}
    for k in range(j):
      if S[k] in f.keys():
        f[S[k]] += 1
      else:
        f[S[k]] = 1
        
    for k in range(N-j):
      if S[N-k-1] in b.keys():
        b[S[N-k-1]] += 1
      else:
        b[S[N-k-1]] = 1

    for k in range(N):
      common = 0
      for l in f.keys():
        if l in b.keys():
          common += 1
     
      if common > ans:
        ans = common
        
print(ans)
