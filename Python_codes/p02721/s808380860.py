N,K,C = map(int,input().split())
S = input()

L = [0 for _ in range(K)]
R = [0 for _ in range(K)]
c = 0
i = 0
while(c < K):
  if S[i] == 'o':
    L[c] = i
    c += 1
    i += C+1
  else:
    i += 1
i = N-1
c = K-1
while(c >= 0):
  if S[i] == 'o':
    R[c] = i
    c -= 1
    i -= C+1
  else:
    i -= 1
#print(L)
#print(R)

ans = []
for i in range(K):
  if L[i] == R[i]:
    ans.append(L[i])
for a in ans:
  print(a+1)
