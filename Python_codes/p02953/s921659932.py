N = int(input())

H = list(map(int, input().split()))
for i in range(1,N+1):
    tmp = H[-i]
    if not i==N:
        if tmp < H[-i-1]:
            if tmp == H[-i-1]-1:
                H[-i-1] -= 1
            else:
                print('No')
                exit()
print('Yes')
