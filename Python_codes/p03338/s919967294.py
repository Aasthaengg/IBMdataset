N = int(input())
S = input()
ans = 0

for n in range(N-1):
  c = 0
  A = list(set(S[:n+1]))
  B = list(set(S[n+1:]))
  for a in A:
    if a in B:
      c+=1
  ans = max(ans,c)
  
print(ans)