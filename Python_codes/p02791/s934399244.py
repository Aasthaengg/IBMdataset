N = int(input())
P = list(map(int, input().split()))
count = 1
m = P[0]
for i in range(1, N):
  if P[i] < m:
    m = P[i]
    count += 1
print(count)