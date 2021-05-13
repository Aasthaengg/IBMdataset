S = input()
s = {"A", "C", "G", "T"}
ans = 0
tmp = 0
for i in S:
  if i in s:
    tmp += 1
    ans = max(ans, tmp)
  else:
    tmp = 0
print(ans)