x = input()
z = 1
y = x[0]
for i in x[1:]:
      if (y == i):
            print("Bad")
            z = 0
            break
      y = i
if (z!= 0):
      print("Good")
