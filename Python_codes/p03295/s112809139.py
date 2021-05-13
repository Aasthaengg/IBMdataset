n,m = map(int,input().split())
req = [list(map(int,input().split())) for i in range(m)]

req.sort(key=lambda x: x[1])

cnt=0
for i in range(m):
    
    if(i==0):
        last = req[i][1]
        cnt+=1
        continue
    now = req[i][0]
    if(now < last):
        continue
    last = req[i][1]
    cnt+=1

print(cnt)
