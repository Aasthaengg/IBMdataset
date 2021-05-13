A,B = list(map(int,input().split()))
ans = 1
for i in range(10**18):
    if A * 2 <= B:
        A *= 2
        ans +=1
    else:
        print(ans)
        exit()