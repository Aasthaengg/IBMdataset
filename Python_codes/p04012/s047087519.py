W = input()
for w in W:
  if W.count(w)&1:
    print("No")
    break
else:
  print("Yes")