s = list(input())
for index, i in enumerate(s):
  if i == "?":
    s[index] = "D"
ans = "".join(s)
print(ans)