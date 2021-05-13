import array
N, K = map(int, input().split(' '))

minimum = x = N % K

cache = set()
while True:
    x = abs(x - K)
    minimum = min(x, minimum)
    if x in cache:
        break
    else:
        cache.add(x)

print(minimum)
