N = int(input())
H = list(map(int,input().split()))
tot = 0
while True:
    if H[0]>0:
        cnt = 1
    else:
        cnt = 0
    for i in range(1,N):
        if H[i]>0 and H[i-1]==0:
            cnt += 1
    tot += cnt
    for i in range(N):
        if H[i]>0:
            H[i] -= 1
    flag = 0
    for i in range(N):
        if H[i]>0:
            flag = 1
            break
    if flag==0:break
print(tot)    