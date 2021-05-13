import math

k = input()
k = int(k)

les = math.ceil( k / 1000)

ans = 1000 * les - k
print(ans)