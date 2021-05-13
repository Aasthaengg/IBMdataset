N = int(input())
sum = 0

for _ in range(N):
  b, e = map(int, input().split())
  sum += abs(e - b) + 1

print(sum)