s = input().split(" ")
a,b = int(s[0]), int(s[1])
if (a*3 + b) % 2 == 0:
  print(int((a*3 + b)/2))
else:
  print(int((a*3 + b - 1)/2))