N, T = map(int, input().split())
A = list(map(int, input().split()))

INF = 10**10
L_min = [INF] * N
for i in range(N):
  L_min[i] = min(L_min[i-1], A[i])
#print(L_min)

P_max = -1
for i in range(N):
  P_max = max(P_max, A[i] - L_min[i])
#print(P_max)

answer = 0
for i in range(N):
  if P_max == A[i] - L_min[i]:
    answer += 1
print(answer)