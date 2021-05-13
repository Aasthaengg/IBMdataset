S = str(input())

if S.endswith('s'):
  S += "es"
else:
  S += "s"
print(S)