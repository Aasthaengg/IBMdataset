h,w = map(int,input().split())
n = int(input())
a = list(map(int,input().split()))

ans = [[0 for j in range(w)] for i in range(h)]

x = 0
y = 0
f = True
for i in range(n):
    for j in range(a[i]):
        ans[y][x] = str(i+1)
        if f:
            x += 1
        else:
            x -= 1
        if x == w:
            x = w-1
            y += 1
            f = False
        if x == -1:
            x = 0
            y += 1
            f = True

for i in range(h):
    print(" ".join(ans[i]))


