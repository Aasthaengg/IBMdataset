N = int(input())
s = input()
t = input()
ans = 2 * N
for i in range(N):
  if s[i:] == t[:N-i]:
    ans = N + i
    break
print(ans)