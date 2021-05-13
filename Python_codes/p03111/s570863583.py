n,A,B,C = map(int,input().split())
L = [int(input()) for _ in range(n)]

ans = float('inf')
for i in range(2**n):
    for j in range(2**n):
        where = [0]*n
        x,y = i,j
        b = 0
        while x > 0 or y > 0:
            where[b] += (x&1) + 2*(y&1)
            b += 1
            x,y = x >> 1 , y >> 1
        cnt = -30
        ABC = [0,0,0]
        for x,w in enumerate(where):
            if w == 0:continue
            ABC[w-1] += L[x]
            cnt += 10
        if 0 in ABC:continue
        ans = min(ans, cnt + abs(ABC[0] - A) + abs(ABC[1] - B) + abs(ABC[2] - C))
print(ans)
