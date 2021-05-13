n, k = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[0])
start = 1
end = 0
for i in range(n):
    a, b = ab[i]
    end += b
    if start <= k <= end:
        print(a)
        exit()
    start += b
