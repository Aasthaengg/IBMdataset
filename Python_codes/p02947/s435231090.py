N = int(input())
S = []
for _ in range(N):
    S.append(input())
for i in range(N):
  S[i] = sorted(S[i])
  S[i] = ''.join(S[i])

t = {}
for i in range(N):
  if S[i] in t:
    t[S[i]] += 1
  else:
    t[S[i]] = 1
 
print(sum(t[k]*(t[k]-1)//2 for k in t))