N, x = list(map(int,input().split()))
a = list(map(int,input().split()))
result = 0

for i in range(N-1):
  n = a[i] + a[i+1] - x
  if n > 0:
    result += n
    a[i+1] -= n
    if a[i+1] < 0:
      a[i+1] = 0

print(result)