n, k = map(int, input().split())
h = [0]*k

while True:
    for j in range(k):
        h[j] += 1
        n -= 1
        if n <= 0:
            print(max(h) - min(h))
            exit()

