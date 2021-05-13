s = input()
ans = ""
for i,x in enumerate(s):
  if i%2 == 0:
    ans += x
print(ans)