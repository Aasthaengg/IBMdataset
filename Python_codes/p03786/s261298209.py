N = int(input())
A = sorted(list(map(int, input().split())))
dp = {}
quota = 0
res = 0
size = 0
streak = 1
for i in range(N-1):
  a = A[i]
  size += a
  if A[i+1] <= size*2:
    streak += 1
  else:
    streak = 1

print(streak)
