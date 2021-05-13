N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]
L.sort(key=lambda x: x[1])
w = 0
for x,y in L:
    w += x
    if w > y:
        print('No')
        exit()
print('Yes')