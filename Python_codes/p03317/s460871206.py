
import math
N,K = map(int,input().split())
A = list(map(int,input().split()))


N -= K

print(math.ceil(N/(K-1))+1)