inputLine = [int(i) for i in input().split()]
L = inputLine[0]
R = inputLine[1]
d = inputLine[2]
count = 0
for x in range(L,R+1):
  if ( x%d == 0 ):
    count += 1
    
print(count)