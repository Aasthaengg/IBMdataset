N = int(input())
A = list(map(int, input().split()))
count = 0

for i in range(N):
  if A[A[i]-1] == i + 1:
    count += 1

print(int(count / 2))