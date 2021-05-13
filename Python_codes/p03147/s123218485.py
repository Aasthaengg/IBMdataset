N = int(input())
H = list(map(int, input().split()))

ans = 0
zero = 0

for h in H:
    if h == 0:
        zero += 1

while zero < N:
    flg = False
    cnt = 0

    for i in range(N):
        if H[i] > 0:
            flg = True
            H[i] -= 1

            if H[i] == 0:
                zero += 1
        else:
            if flg:
                cnt += 1
                flg = False

    if flg:
        cnt  += 1

    ans += cnt


print(ans)
