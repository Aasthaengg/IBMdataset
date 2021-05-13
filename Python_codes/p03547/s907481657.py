a,b =list(input().split())
if ord(a) < ord(b):
  print("<")
elif ord(b) < ord(a):
  print(">")
else:
  print("=")