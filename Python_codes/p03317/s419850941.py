import math
N, K = map(int, input().split())
A = input()
print(math.ceil((N-K)/(K-1))+1)