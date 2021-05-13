import math
n, k = map(int, input().split())
a = [int(i) for i in input().split()]


print(int(math.ceil((len(a)-1) / ( k -1))))