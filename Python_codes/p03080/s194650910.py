n = int(input())
sl = list(input())

c = sl.count("R")

if c > n-c:
   print("Yes")
else:
   print("No")