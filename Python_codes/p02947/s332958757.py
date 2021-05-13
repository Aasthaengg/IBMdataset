n = int(input())
s = {}

for i in range(n):
  tmp = ''.join(sorted(input()))
  if tmp in s:
    s[tmp] += 1
  else:
    s[tmp] = 1

ans = 0
for i in s.values():
  if i >= 2:
    ans += i*(i-1)/2
print(int(ans))