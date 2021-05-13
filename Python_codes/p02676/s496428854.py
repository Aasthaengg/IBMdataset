k=int(input())
s=str(input())
if len(s)<=k:
  print(s)
  exit()
else:
  print(s[0:k]+"...")