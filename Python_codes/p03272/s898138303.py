import sys

input = input().split()
total = int(input[0])
front = int(input[1])

if(total<1 or total>100):
  sys.stderr.write('Error occurred!')
elif(front<1 or front > total):
  sys.stderr.write('Error occurred!')
else:  
  locationFromBack = (total-front) + 1
  print(locationFromBack)