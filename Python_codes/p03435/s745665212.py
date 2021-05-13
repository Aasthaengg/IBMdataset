c = [list(map(int, input().split())) for _ in range(3)]
flg = True
s = sum(c[0]) % 3
t = sum(c[i][0] for i in range(3)) % 3
for i in range(1, 3):
  if sum(c[i]) % 3 != s:
    flg = False
  if sum(c[j][i] for j in range(3)) % 3 != t:
    flg = False
if flg:
  print("Yes")
else:
  print("No")