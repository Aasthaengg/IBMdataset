h, w = map(int, input().split())
a = [list(input()) for i in range(h)]
for i in range(h) :
    a[i].insert(0, "#")
    a[i].append("#")
print("#"*(w+2))
for i in range(h) :
    for j in range(w+2) :
        print(a[i][j],sep="",end="")
    print("")
print("#"*(w+2))
