n,h,w = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
for x,y in li:
    if x >= h and y >= w:
        cnt += 1
        
print(cnt)