N = int(input())
A = list(map(int,input().split()))

ans = 0
temp = 0
for n in range(N):
  x = 0
  temp = A[n]
  while x == 0:
    if temp % 2 == 0:
      ans += 1
      temp = temp //2
    else:
      x = 1
print(ans)