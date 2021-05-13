n = int(input())
s = input()
t = input()
for i in range(n):
  cnt = 0
  for j in range(i, n):
    if s[j] != t[j-i]:
      break
    cnt += 1
  if cnt == n-i:
    ans = n+i
    break
if cnt == 0:
  ans = 2*n
print(ans)
