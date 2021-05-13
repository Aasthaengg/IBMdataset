N = int(input())
h = list(map(int, input().split()))

sumh = h[0]
for x in range(N):
    if x != N - 1:
        if h[x + 1] > h[x]:
            sumh += h[x + 1] - h[x]
print(sumh)
