tmp = input().split(" ")
total = int(tmp[0])
leg = int(tmp[1])
 
if leg % 2 == 0 and 4 * total >= leg >= 2 * total:
  print("Yes")
else:
  print("No")