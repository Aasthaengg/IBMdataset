key = list(map(int, input().split()))
if 2 in key:
  print("No")
elif (key[0] in [4, 6, 9, 11] and key[1] in [4, 6, 9, 11]) or (key[0] in [1, 3, 5, 7, 8, 10, 12] and key[1] in [1, 3, 5, 7, 8, 10, 12]):
  print("Yes")
else:
  print("No")