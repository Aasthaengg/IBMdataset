h, w = map(int, input().split())

c = [list(input()) for _ in range(h)]
for i in range(h):
    for _ in range(2):
        for j in range(w):
            print(c[i][j], end = "")
        
        print()