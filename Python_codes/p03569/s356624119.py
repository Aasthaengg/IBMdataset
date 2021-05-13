s = input()
l = 0
r = len(s)-1
c = 0
if s.count("x") == len(s):
  print(0)
  exit()
while l < r:
  c_l = 0
  c_r = 0
  while s[l] == "x":
    c_l += 1
    l += 1
  while s[r] == "x":
    c_r += 1
    r -= 1
  if s[l] != s[r]:
    print(-1)
    exit()
  c += abs(c_l-c_r)
  l += 1
  r -= 1
print(c)