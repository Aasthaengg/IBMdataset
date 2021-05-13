a,b,k = map(int,input().split())

cnt = 1
for i in range(a,b+1):
    if cnt <= k:
        print(i)
    elif cnt > b-a+1 - k:
        print(i)
    cnt += 1

