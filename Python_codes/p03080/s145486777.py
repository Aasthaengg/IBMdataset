N=int(input())
s=input()
num_blue = s.count("B")
num_red = s.count("R")

if num_red > num_blue:
  print("Yes")
else:
  print("No")