k = int(input())
a,b = list(map(int, input().split()))

n = a//k
ans = n * k
while ans <= b:
  if a <= ans <= b:
    exit(print('OK'))
  else:
    n += 1
    ans = k * n

print('NG')