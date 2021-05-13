import collections
import math
def Comb(N,R):
    return math.factorial(N)//(math.factorial(N-R)*math.factorial(R))

N = int(input())
S = ['']*N
for T in range(0,N):
    S[T] = ''.join(sorted(input()))
Count = list(collections.Counter(S).values())
Sum = 0
for TT in range(0,len(Count)):
    if Count[TT]>=2:
        Sum += Comb(Count[TT],2)
print(Sum)