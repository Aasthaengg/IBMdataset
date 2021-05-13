h,w = map(int,input().split())
c = [0]*h
for i in range(h):
    c[i] = list(input())
for i in range(h):
    for _ in range(2):
        for j in range(w):
            print(c[i][j],end='')
        print("")