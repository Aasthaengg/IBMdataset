N, M = map(int, input().split())
T = set([*range(1, M+1)])
for _ in range(N):
  K, *A = map(int, input().split())
  T = T&set(A)
print(len(T))