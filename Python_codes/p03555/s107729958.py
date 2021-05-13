C1 = input()
C2 = input()
ans = 'YES'
if C1[0] != C2[2]:
  ans = 'NO'
if C1[1] != C2[1]:
  ans = 'NO'
if C1[2] != C2[0]:
  ans = 'NO'
print(ans)