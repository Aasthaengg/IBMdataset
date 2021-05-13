import math
N = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))
S = [abs(x-y) for x,y in zip(X, Y)]
SS = [s**2 for s in S]
SSS = [s**3 for s in S]
print(sum(S))
print(pow(sum(SS), 1/2))
print(pow(sum(SSS), 1/3))
print(max(S))
