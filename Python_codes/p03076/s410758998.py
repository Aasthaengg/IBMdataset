from itertools import permutations
import math
X = [int(input()) for _ in range(5)]
Time = lambda X: sum(math.ceil(X[i]/10)*10 for i in range(4))+X[-1]
print(min(Time(x) for x in permutations(X)))