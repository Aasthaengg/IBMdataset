h,w,a,b = map(int,input().split())
s = [["0"]*w for _ in range(h)]
for i in range(b):
    for j in range(a): s[i][j] = "1"
for i in range(h-b):
    for j in range(w-a):
        s[h-1-i][w-1-j]: s[i][j] = "1"
for i in range(h): print("".join(s[i]))