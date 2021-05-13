N = int(input())
P = list(map(int, input().split()))
count = 0
for n in range(1, N - 1):
  if (P[n] > P[n - 1] and P[n] < P[n + 1]) or (P[n] < P[n - 1] and P[n] > P[n + 1]):
    count += 1
print(count)