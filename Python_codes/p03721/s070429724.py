n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
length = 0
for x in sorted(ab, key=lambda x: x[0]):
    length += x[1]
    if length >= k:
        print(x[0])
        break