s = input()
ans = "AC"
if s[0] == "A":
  c_cnt = 0
  for i in range(2,len(s)-1):
    if s[i] == "C":
      c_cnt += 1
  if c_cnt == 1:
    for i in s:
      if i.lower() != "a" and i.lower() != "c" and i.lower() != i:
        ans = "WA"
        break
  else:
    ans = "WA"
else:
  ans = "WA"
print(ans)