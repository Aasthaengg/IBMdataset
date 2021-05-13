N = int(input())
s = list(input())
t = list(input())
ans = 2*N
for i in range(N):
  if s[i:] == t[:(N-i)]:
    ans = N+i
    break
print(ans)