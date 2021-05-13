N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0
for i in A:
  if i >= K:
    count += 1
print(count)