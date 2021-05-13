N = int(input())
K = 101
D = []
for _ in range(N):
    x, y, h = map(int, input().split())
    D.append((x,y,h))
D.sort(key=lambda x:x[2], reverse=True)
for i in range(K):
    for j in range(K):
        flg = True
        H = -1
        for x, y, h in D:
            if h == 0:
                if H > abs(x-i) + abs(y-j):
                    flg = False
                    break
                continue
            if H == -1:
                H = abs(x-i) + abs(y-j) + h
                continue
            if H != abs(x-i) + abs(y-j) + h:
                flg = False
                break
        if flg:
            print(i,j,H)
            exit()
