import math
n=int(input())
xc=math.ceil(n/1.08)
nn=xc*1.08
if math.floor(nn)==n:    
	print(xc)
else:
  print(":(")
