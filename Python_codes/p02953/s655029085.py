n = int(input())
H = list(map(int, input().split()))
for i in range(1, n):
    if H[i - 1] < H[i]:
        H[i] -= 1
    elif H[i - 1] > H[i]:
        print('No')
        exit()
print('Yes')