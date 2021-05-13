n = int(input())
la = list(map(int, input().split()))
ans = 10**10
for i in la:
  tmp = 0
  while i%2 == 0:
    i = i/2
    tmp += 1
  ans = min(ans, tmp)
print(ans)