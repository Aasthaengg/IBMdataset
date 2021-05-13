S = input()
a = "abcdefghijklmnopqrstuvwxyz"
ans = "None"
for x in a:
  if x not in S:
    ans = x
    break
print(ans)