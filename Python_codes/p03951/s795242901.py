N = int(input())
s = input()
t = input()
ans = 2*N
for i in range(N):
  ss = s[i:N]
  tt = t[0:N-i]
  if (ss == tt):
    ans = N+i
    break
print(ans)