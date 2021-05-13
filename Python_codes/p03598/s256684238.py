import numpy as np

N = int(input())
K = int(input())
X = np.array(input().split(), int)
Y = K - X

ans = [2 * min(x,y) for x,y in zip(X,Y)]
print(sum(ans))