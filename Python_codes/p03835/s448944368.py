K,S = input().strip().split()
K,S = int(K),int(S)

count = 0

for x in range(S+1):
  for y in range(S+1-x):
    z = S - x- y
    #print( x,y,z)
    if x <= K and y <= K and z <= K:
      count += 1
print(count)