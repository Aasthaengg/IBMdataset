#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]


h,w = map(int, input().split())
s = [list(input()) for _ in range(h)]

dx = [ 0, -1, -1, -1,  0,  1, 1, 1 ]
dy = [ 1,  1,  0, -1, -1, -1, 0, 1 ]

for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            cnt = 0
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if ( x >= 0 and x < h and y >=0 and y < w):
                    if (s[x][y] == "#"):
                        cnt+=1
            s[i][j] = str(cnt)
#print(s)

for i in range(h):
    for j in range(w):
        print(s[i][j], end="")
    print("")



