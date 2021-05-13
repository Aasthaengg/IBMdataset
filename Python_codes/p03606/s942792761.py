N = int(input())
A = 0
for i in range(N):
  l = list(map(int, input().split()))
  A += l[1] - l[0] + 1
print(A)