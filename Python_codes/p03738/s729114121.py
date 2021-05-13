a = input()
b = input()

lena=len(a)
lenb=len(b)

s = [a,b]
s.sort()

ans = 0
if lena>lenb:
  ans = a
elif lena<lenb:
  ans = b
elif s[0] == s[1]:
  ans = 0
else:
  ans = s[1]
  
if ans==0:
  print("EQUAL")
elif ans==a:
  print("GREATER")
else:
  print("LESS")
