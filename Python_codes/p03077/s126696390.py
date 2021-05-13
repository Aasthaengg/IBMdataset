import math
N = int(input())
X = [int(input()) for i in range(5)]
mc = min(X)
mci = X.index(mc)
print(4 + math.ceil(N/mc))