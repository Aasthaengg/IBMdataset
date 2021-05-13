N = int(input())
a = [int(input()) - 1 for _ in range(N)]

light = 0
visited = [False] * N
count = 0
while True:
    if light == 1:
        break

    if visited[light]:
        print(-1)
        exit(0)

    visited[light] = True
    light = a[light]
    count += 1

print(count)
