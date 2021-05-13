N, M = map(int, input().split())
min = 1000000000
sum = 0
for i in range(N):
  j = int(input())
  if min > j:
    min = j
  M -= j
  sum += 1
print(sum + M // min)
