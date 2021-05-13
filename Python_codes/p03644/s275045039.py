n = int(input())
ANS = 1
keep = 0
for i in range(1,n+1):
  check = i
  ans = 0
  while check % 2 == 0:
    check = check // 2
    ans += 1
  if keep < ans:
    keep = ans
    ANS = i
print(ANS)
