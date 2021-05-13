K = int(input())
A = list(map(int, input().split()))
min = 2
max = 2
for i in range(K-1, -1, -1):
    min += (-min) % A[i]
    max -= max % A[i]
    max += A[i] - 1
if max < min:
  print(-1)
  exit()
print(min, max)
