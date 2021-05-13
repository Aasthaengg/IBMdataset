#ABCがBCAになる
#ADがDAになる
s = input()
s = s.replace("BC", "D")

c_A = 0
ans = 0
for v in s:
  if v == "A":
    c_A += 1
  elif v == "D":
    ans += c_A
  else:
    c_A = 0
print(ans)