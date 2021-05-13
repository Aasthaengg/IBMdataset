import sys
 
input = sys.stdin.readlines()
 
n = int(input[0])
hatList = list(input[1])
counter = 0

for i in range (n):
  if(hatList[i] == "R"):
    counter += 1
    
if counter > (n/2):
    print("Yes")
else:
	print("No")