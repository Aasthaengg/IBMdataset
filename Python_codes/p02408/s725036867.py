n = int(raw_input())
 
c = {"S":[0]*13, "H":[0]*13, "C":[0]*13, "D":[0]*13} 
  
for i in range(n):
  mark, num = raw_input().split()
  c[mark][int(num)-1] = 1
  
for k in ["S", "H", "C", "D"]:
  for j in range(13):
    if c[k][j] == 0:
      print "%s %d" % (k, j+1)