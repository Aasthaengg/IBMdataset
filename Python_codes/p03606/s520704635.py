N = int(input())

ans = 0
for i in range(N):
  b1, b2 = map(int,input().split())
  c = b2-b1+1
  ans += c

print(ans)