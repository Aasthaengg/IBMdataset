N = int(input())
T, A = input().split(' ')
T = int(T)
A = int(A)
H = input().split(' ')
H = [int(H[i]) for i in range(N)]
check = 10**9
for i in range(N):
  C = A - (T - H[i] * 0.006)
  if abs(C)<check:
    check = abs(C)
    point = i + 1
print(point)