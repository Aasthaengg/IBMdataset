s = input()
ans = 0
curr = 0
for i in range(3):
  if s[i]== "R":
    curr += 1
  else:
    ans = max(ans, curr)
    curr =0
else:
  ans = max(ans, curr)
print(ans)