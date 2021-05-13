import math

N,K = [int(x) for x in input().split()]

div = N//K

print(min(N-div*K,abs(N-(div+1)*K)))