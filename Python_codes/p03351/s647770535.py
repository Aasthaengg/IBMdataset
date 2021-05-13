l = [int(x) for x in input().split(" ")]
if abs(l[0]-l[2]) <= l[3]:
  print("Yes")
elif abs(l[0]-l[1]) <= l[3] and abs(l[1]-l[2]) <= l[3]:
  print("Yes")
else:
  print('No')