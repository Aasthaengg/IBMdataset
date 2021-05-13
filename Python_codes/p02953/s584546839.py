N = int(input())

H = list(map(int, input().split()))
flg = False
for i in range(1,N+1):
    if flg:
        tmp = H[-i]-1
    else:
        tmp = H[-i]
    flg = False
    if not i==N:
        if tmp < H[-i-1]:
            if tmp == H[-i-1]-1:
                flg = True
            else:
                print('No')
                exit()
print('Yes')