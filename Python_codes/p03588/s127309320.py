N = int(input())
A = []
B = []
for _ in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)
print(min(B)+max(A))