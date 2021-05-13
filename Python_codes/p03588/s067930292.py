N = int(input())
M = 0
m = 10**9
c = 0
for i in range(N):
  a,b = map(int,input().split())
  if m >= a:
    m = a
  if M < a:
    M = a
    c = b + 1
ans = c+M-1
print(ans)
