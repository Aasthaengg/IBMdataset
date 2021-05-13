n = int(input())
a = [list(map(int,input().split()))for _ in range(n)]
ans = 0
for x1,y1 in a:
    for x2,y2 in a:
        ans += ((x1-x2)**2+(y1-y2)**2)**0.5
print(ans/n)