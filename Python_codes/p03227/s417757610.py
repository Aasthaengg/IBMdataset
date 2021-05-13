S=list(input())

if len(S)==2:
  print("".join(S))
else:
  S.reverse()
  print("".join(S))