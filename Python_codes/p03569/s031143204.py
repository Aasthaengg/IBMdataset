s = input()
len_s = len(s)
a = [i for i in s if i != "x"]
b = "".join(a)
if b != b[::-1]:
  print(-1)
  exit()
ans = 0
f,r = 0,len_s-1
while f < r:
  if s[f] == s[r]:
    f += 1
    r -= 1
  elif s[f] == "x":
    f += 1
    ans += 1
  elif s[r] == "x":
    r -= 1
    ans += 1
print(ans)