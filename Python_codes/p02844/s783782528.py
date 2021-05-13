N = int(input())
S = input()
P, Q = [], [] 
t = 0
for i in range(N-2):
  if S[i] not in P:
    P.append(S[i]) 
    for j in range(i+1, N-1):
      if S[j] not in Q:
        Q.append(S[j])
        t += len(set(S[j+1:]))
    Q.clear()
print(t)