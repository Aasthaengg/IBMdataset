a, b, k = map(int, input().split())

if b - a < 2 * k:
    for v in range(a, b+1):
        print(v)
else:
    for v in range(a, a+k):
        print(v)
    for v in range(b-k+1, b+1):
        print(v)