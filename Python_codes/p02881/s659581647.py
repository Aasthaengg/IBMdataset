import math
 
N = int(input())
 
for i in reversed(range(int(math.sqrt(N))+1)):
  if N % i == 0:
    print(i-1+(N//i)-1)
    break