n,h,w = list(map(int, input().split())) 
sizeList = [list(map(int, input().split()))  for _ in range(n)]

cnt = 0
for row in sizeList:
    if( row[0] >= h and row[1] >= w):
        cnt += 1
print(cnt)
