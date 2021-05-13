N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
ans = 0
m = A + 1000
for i in range(N):
  d = abs(T - H[i] * 0.006 - A)
  if m > d:
    m = d
    ans = i + 1
print(ans)