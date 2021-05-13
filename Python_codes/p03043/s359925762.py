import math
N,K  = (int(x) for x in input().split())
Win  = list(max(math.ceil(math.log2(K/X)),0) for X in range(1,N+1))
Prob = sum(1/(N*pow(2,X)) for X in Win)
print(Prob)