import math
N,K = map(int,input().split())
L = [i for i in map(int,input().split())]
#if (N-1) % (K-1) != 0:
  #print(((N-1)//(K-1))+1)
#else:
  #print((N-1) % (K-1)) #equivalent to ceil.
print(math.ceil((N-1)/(K-1)))