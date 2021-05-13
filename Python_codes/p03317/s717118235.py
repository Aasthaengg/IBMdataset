import math

N,K = map(int,input().split())
A = list(map(int,input().split()))

N -= K
K -= 1
C = math.ceil(N/K)

print(C+1)
