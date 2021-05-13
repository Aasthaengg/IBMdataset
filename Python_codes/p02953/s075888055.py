n = int(input())
H = list(map(int, input().split()))
for i in range(1, n):
    if H[i] < H[i-1]:
        print('No')
        exit()
    else:
        if H[i] > H[i-1]:
            H[i] -= 1
else:
    print('Yes')
