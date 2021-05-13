n,h,w = map(int,input().split())
a = [list(map(int,input().split())) for i in range(n)]
p = 0

for i in range(n):
    if a[i][0] >= h and a[i][1] >= w:
        p += 1

print(p)