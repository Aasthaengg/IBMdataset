x,y = list(map(int,input().split()))
MIN = float('inf')
for i in [1,-1]:
    for j in [1,-1]:
        ans = 0
        tmpx = x
        if i == -1:
            tmpx = i*tmpx
            ans += 1
        tmpx += abs(abs(x)-abs(y))
        ans += abs(abs(x)-abs(y))
        if j == -1:
            tmpx = j*tmpx
            ans += 1
        if tmpx == y:
            MIN = min(MIN,ans)
print(MIN)