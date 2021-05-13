N = int(input())
s = list(map(int, input().split()))
A = 1
for i in range(N):
  A *= s[i-1]

B = 0
for i in range(N):
  B += A/s[i-1]

K = A/B
print(K)
