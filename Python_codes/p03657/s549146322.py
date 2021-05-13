ary = input().split(" ")
A = int(ary[0])
B = int(ary[1])
 
if A % 3 == 0 or B % 3 == 0 or (A + B) % 3 == 0:
  print("Possible")
else:
  print("Impossible")