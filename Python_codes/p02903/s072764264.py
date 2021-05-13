h,w,a,b = [int(x) for x in input().split()]
m = [["1"]*w for i in range(h)]
for i in range(h):
    for j in range(w):
        if i<=b-1 and j<=a-1:
            m[i][j] = "0"
        if i>b-1 and j>a-1:
            m[i][j] = "0"
        
for i in range(h):
    s = ""
    for j in range(w):
        s += m[i][j]
    print(s)