l,r,d=map(int, input().split())

cnt = 0
tmp = 0

while tmp <= r:
    tmp = tmp + d
    if tmp >= l and tmp <= r:
        cnt+=1

print(cnt)