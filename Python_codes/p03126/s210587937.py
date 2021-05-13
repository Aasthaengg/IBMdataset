N, M = list(map(lambda a: int(a), input().split(" ")))
P = [(i + 1) for i in range(M)]
s = []
for j in range(N):
  A = list(map(lambda x: int(x), input().split(" ")))
  s.append(A[1:])
  
for k in range(len(s)):
  P = list(set(P) & set(s[k]))


print(len(P))