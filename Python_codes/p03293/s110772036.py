S=input()
T=input()
N=len(S)
for i in range(N):
  s=S[-1]+S[:-1]
  if s==T:
    print('Yes')
    exit(0)
  else:
    S=s
print('No')