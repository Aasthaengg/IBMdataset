h, w = map(int, input().split())
img = [list(input()) for i in range(h)]
out = [[0 for j in range(w)] for i in range(2*h)]
for i in range(2*h) :
    for j in range(w) :
        out[i][j] = img[int(i/2)][j]
for i in range(2*h) :
    for j in range(w) :
        print(out[i][j],sep="",end="")
    print("")
