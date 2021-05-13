import sys
N = int(input())
s = input()
t = input()
ans = s+t
for i in range(N):
  if s[i:N] == t[0:N-i]:
    ans = s[0:i]+s[i:N]+t[N-i:N]
    break
print(len(ans))