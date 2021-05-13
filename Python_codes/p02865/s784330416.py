N = int(input())
A = [i for i in range(1, N)]
ans = 0
for i in range(N//2):
  a, b = A[i], A[N-2-i]
  if N == (a+b) and a != b:
    ans += 1
print(ans)    