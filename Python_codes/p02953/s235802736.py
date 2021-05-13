N = int(input())
H = list(map(int, input().split()))

flg = 1
for i in range(N-1):
    if H[i+1] - 1 >= H[i]:
        H[i+1] -= 1
    elif H[i+1] < H[i]:
        flg = 0
        break
if flg == 1:
    print('Yes')
elif flg == 0:
    print('No')