S = input()
ans = "None"
for i in range(97, 123):
  alp = chr(i)
  if alp not in S:
    ans = alp
    break
print(ans)