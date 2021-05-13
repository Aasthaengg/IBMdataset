n = int(input())
a = [111,222,333,444,555,666,777,888,999]
ans = 0
for i in a:
  if n > i:
    continue
  ans = i
  break

print(ans)