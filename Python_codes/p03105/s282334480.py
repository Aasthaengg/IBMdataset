s=list(map(int,input().split()))
a=s[1]//s[0]
if a<=s[2]:
  print(int(a))
else:
  print(s[2])