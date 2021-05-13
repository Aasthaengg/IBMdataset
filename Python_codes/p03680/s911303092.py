from sys import exit

n = int(input())
a = [int(input()) for _ in range(n)]

visited = [False] * n
res = 0
button = 0
while True:
    visited[button] = True
    button = a[button] - 1
    res += 1

    if visited[button]:
        print(-1)
        exit()
    
    if button == 1:
        print(res)
        exit()