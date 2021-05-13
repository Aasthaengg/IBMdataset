n = int(input())
S = []
# c1:Bで始まってAで終わるもの
# c2:Bで始まるが、A以外で終わるもの
# c3:Bで始まらないが、Aで終わるもの
# c4:Bでも始まらないし、Aでも終わらないもの

ans = 0
c1 = 0
c2 = 0
c3 = 0
for _ in range(n):
  s = input()
  ans += s.count("AB")
  if s.startswith("B") and s.endswith("A"):
    c1 += 1
  elif s.startswith("B"):
    c2 += 1
  elif s.endswith("A"):
    c3 += 1
if c2 + c3 > 0:
  ans += min(c1+c2, c1+c3)
else:
  if c1 != 0:
    ans += c1 - 1
print(ans)


