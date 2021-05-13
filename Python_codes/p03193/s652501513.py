n,h,w = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for a,b in ab:
    if h <= a and w <= b:
        cnt += 1
print(cnt)