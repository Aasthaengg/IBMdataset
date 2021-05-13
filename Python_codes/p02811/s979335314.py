tmp = input().split(" ")
 
N = int(tmp[0])
X = int(tmp[1])
 
if X <= 500 * N:
  print("Yes")
else:
  print("No")