import math
NXT = [int(i) for i in input().split()]
N = NXT[0]
X = NXT[1]
T = NXT[2]
print((math.ceil(N/X))*T)