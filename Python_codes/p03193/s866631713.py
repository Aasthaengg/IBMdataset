n,h,w = map(int,input().split())
ans = 0
for i in range(n):
    x,y = map(int,input().split())

    if x >= h and y >= w:
        ans += 1
print(ans)