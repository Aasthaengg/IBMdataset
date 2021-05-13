import math
for d in iter(input, '0'):
    n, s = int(d), list(map(int, input().split()))
    print(math.sqrt(sum([si**2 for si in s])/n - (sum(s)/n)**2))