N,K = map(int,input().split())
odd_count = 0
even_count = 0
ans = 0

for i in range(1,N+1):
  if i%K == 0:
    odd_count += 1
  elif i%K == K//2:
    even_count += 1

if K%2 != 0:
  ans = odd_count**3
else:
  ans = odd_count**3 + even_count**3

print(ans)