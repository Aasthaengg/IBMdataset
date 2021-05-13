ls = list(str(s) for s in input().split())
ans = []
for s in ls:
  ans.append(s[0].upper())
print("".join(ans))