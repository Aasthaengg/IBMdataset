N, K = map(int, input().split())
x = []
for i in range(N):
    a, b = map(int, input().split())
    x.append([a, b])

x.sort(key=lambda x: x[0])

c = 0
for a, b in x:
    c += b
    if K <= c:
        print(a)
        exit()
