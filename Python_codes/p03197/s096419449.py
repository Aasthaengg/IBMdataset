n = int(input())
ok = True;
for i in range(n):
  a = int(input())
  if a%2==1:
    ok = False
if ok:
  print("second")
else:
  print("first")