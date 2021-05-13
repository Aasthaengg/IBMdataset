s = input()

ans = []
for i, v in enumerate(s):
  if i%2==0:
    ans.append(v)
print("".join(ans))