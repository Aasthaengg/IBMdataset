import math
N = int(input())

change = (math.ceil(N/1000))*1000-N

print(change)