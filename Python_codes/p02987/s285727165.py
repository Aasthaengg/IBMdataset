S1 = input()
S2 = list(S1)
S2.sort()

if S2[0] == S2[1]:
  if S2[1] != S2[2]:
    if S2[2] == S2[3]:
      print("Yes")
    else:
      print("No")
  else:
    print("No")
else:
  print("No")