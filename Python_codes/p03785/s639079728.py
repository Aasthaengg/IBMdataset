N, C, K = map(int, input().split())
Ts = []

for _ in range(N):
  Ts.append(int(input()))
  
Ts.sort()

cnt = 0
i = 0

while i < N:
  j = i
  while j < N and Ts[j] <= Ts[i] + K and j - i + 1 <= C:
    j += 1
  cnt += 1
  i = j
  
print(cnt)