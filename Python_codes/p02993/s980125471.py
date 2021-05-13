passward = input()
ok = True
for i in range(1, len(passward)):
  if passward[i] == passward[i - 1]:
    ok = False
    break

if ok:
  print("Good")
else:
  print("Bad")