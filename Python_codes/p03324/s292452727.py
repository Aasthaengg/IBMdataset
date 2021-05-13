D,N = list(map(int,input().split()))
count = 0
now = 1
while True:
    tmp = now*100**D
    if tmp%(100**(D+1)) != 0:
        count += 1
    if count == N:
        print(tmp)
        exit()
    now += 1