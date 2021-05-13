N = int(input())
a = list(map(int,input().split()))

tmp = 0
for i in a:
  tmp ^= i

ans = a[:]
for i in range(N):
  ans[i] ^= tmp
print(*ans)