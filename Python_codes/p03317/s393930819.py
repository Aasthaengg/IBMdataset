import math
N, K = map(int,input().split())
list_ai = map(int,input().split())
print(math.ceil(1+(N-K)/(K-1)))
