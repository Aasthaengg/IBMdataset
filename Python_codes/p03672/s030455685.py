S = str(input())
N = len(S)
for i in range(1,N):
  T = S[:N-i]
  M = len(T)
  if M%2 != 0:
    continue 
  if T[:M//2] == T[M//2:]:
    print(M)
    exit()