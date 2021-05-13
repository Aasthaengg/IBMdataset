import math
N,K = list(map(int,input().split()))

#print(math.factorial(N)//(math.factorial(K)*math.factorial(N-K)))
print(N-K+1)
