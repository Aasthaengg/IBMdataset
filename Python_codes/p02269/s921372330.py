dic = {}

for i in range(int(input())):
  cmd, arg = input().split()
  if cmd == "insert":
    dic[arg] = 0
  else:
    if arg in dic:
      print("yes")
    else:
      print("no")