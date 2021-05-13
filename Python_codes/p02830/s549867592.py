N = int(input())
S, T = input().split()
L = []
for i in range(2*N):
  if i&1:
    L.append(T[(i-1)//2])
  else:
    L.append(S[i//2])
print("".join(L))