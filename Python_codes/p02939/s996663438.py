S = str(input())
ans = ''
ans2 = ''
con = 0
for s in S:
  ans += s
  if ans != ans2:
    con += 1
    ans2 = ans
    ans = ''
print(con)
      
