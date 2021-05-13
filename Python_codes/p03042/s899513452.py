z = input()
x = int(z[:2])
y = int(z[2:])

if (0<x <= 12):
      if (0<y<= 12):
            print("AMBIGUOUS")
      else:
            print("MMYY")
elif (0<y <= 12):
      if (0<x<= 12):
            print("AMBIGUOUS")
      else:
            print("YYMM")
else:
      print("NA")

