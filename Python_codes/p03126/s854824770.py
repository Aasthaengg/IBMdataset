N, M = map(int, input().split())
K =[set(input().split()[1:]) for _ in range(N)]
T = K[0]
for k in K:
  T = T&k
print(len(T))