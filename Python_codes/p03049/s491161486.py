n = int(input())
a = 0
b = 0
ans = 0
ab = 0
for i in range(n):
  s = input()
  for j in range(len(s)-1):
    if s[j:j+2] == "AB":
      ans += 1
  if s[-1] == "A":
    a += 1
  if s[0] == "B":
    b += 1
  if s[-1] == "A" and s[0] == "B":
    ab += 1
k = min([a, b])

if k == a and k == b and k == ab:
  k -= 1
if k == n:
  k -= 1
if k < 0:
  k = 0
ans += k
print(ans)