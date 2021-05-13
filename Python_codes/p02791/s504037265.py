N = int(input())
P = list(map(int, input().split()))

num = P[0]
count = 1

for i in range(1, N):
  if num >= P[i]:
    count += 1
    num = P[i]

print(count)