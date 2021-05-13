n = int(input())
s = input()

l = 0
r = 1
ans = 0
# 順番に見ていく

while r < n:
  if s[l:r] in s[r:]:
    ans = max(ans, r - l)
    r += 1
  else:
    l += 1
  if l == r:
    l += 1
    r += 2
print(ans)
