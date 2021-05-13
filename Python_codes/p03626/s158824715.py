#17:43
n = int(input())
mod = 10**9 + 7
s = input()
t = [1]
for i in range(1,n):
  if s[i-1] == s[i]:
    t[-1] += 1
  else:
    t.append(1)
#print(t)
l = len(t)
if t[0] == 2:
  ans = 6
else:
  ans = 3
for j in range(1,l):
  if t[j-1] == 1:
    ans *= 2
    ans %= mod
  elif t[j] == 2:
    ans *= 3
    ans %= mod
print(ans)