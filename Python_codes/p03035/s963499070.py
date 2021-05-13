a,b = input().split(" ")
if int(a) >= 13:
  print(b)
elif int(a) in range(6,13):
  print(int(b)//2)
elif int(a) <= 5:
  print(0)