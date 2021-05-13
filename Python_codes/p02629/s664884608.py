n = int(input())

tmp = 0
for ll in range(1,15):
  tmp+=26**ll
  if n <= tmp:
    break

ans = ""
for l in range(1,ll+1):
  n-=1
  ans+=chr(n%26+ord('a'))
  n //= 26
print(ans[::-1])
