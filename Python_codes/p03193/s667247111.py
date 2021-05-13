n,h,w = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
num = 0
for i,j in ab:
    if h <= i and w <= j:
        num += 1
print(num)