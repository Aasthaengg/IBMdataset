n = input()

if len(n) == 1:
  print(n)
  exit()

if all(x == "9" for x in n[1:]):
  ans = n
else:
  ok = False
  ans = ""
  for i, c in enumerate(n):
    x = int(c)
    if x == 9:
      ans += "9"
    else:
      if ok:
        ans += "9"
      else:
        if i == len(n)-1:
          ans = ans[:-1]
          ans += str(int(n[i-1])-1)
          ans += "9"
        else:
          ans += str(x-1)
      ok = True
t = 0
for c in ans:
  x = int(c)
  t += x

print(t)