N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())

for i in range(N - K):
  if T[K + i] == T[i]:
    T[K + i] = 0
    
print(T.count('r') * P + T.count('s') * R + T.count('p') * S)