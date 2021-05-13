N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

x = min([j for i,j in L])

for i,j in L:
    if j == x:
        print(i+j)
        break