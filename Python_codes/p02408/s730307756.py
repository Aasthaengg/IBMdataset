n = int(raw_input())

card = {"S":[0]*13, "H":[0]*13, "C":[0]*13, "D":[0]*13} 
 
for i in range(n):
  mark, nums = raw_input().split()
  card[mark][int(nums)-1] = 1
 
for i in ["S", "H", "C", "D"]:
  for j in range(13):
    if card[i][j] == 0:
      print "%s %d" % (i, j+1)