import math
N, X, T = input().strip().split(' ')
count = math.ceil(int(N)/int(X))
time = int(T) * count
print(time)