A, B = map(lambda S: int(S,16), input().split())
if A < B:
  print("<")
elif A == B:
  print("=")
else:
  print(">")
