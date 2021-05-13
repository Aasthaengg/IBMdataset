n = int(input())
dict = set()
for i in range(n):
  a,b = input().split()
  if a=="insert":
    dict.add(b)
  else:
    if b in dict:
      print("yes")
    else:
      print("no")
