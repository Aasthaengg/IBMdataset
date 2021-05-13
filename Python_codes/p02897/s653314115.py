N = int(input())
ans = 0
if N == 1:
  ans = 1
elif N % 2 == 0:
  ans = 0.5
elif N % 2 == 1:
  ans = (N - (N // 2)) / N
print(ans)