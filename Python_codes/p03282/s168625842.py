s = input()
k = int(input())
rep = s.replace("1", "")
if len(rep) == 0:
  print("1")
else:
  if s.index(rep[0]) < k:
    print(rep[0])
  else:
    print("1")
