N = int(input())
A = list(map(int, input().split()))

ans = 1
mode = 0
prev = A[0]

for i in A:
    check = i - prev

    if check == 0:
        pass
    elif check > 0:
        if mode >= 0:
            mode = check
        else:
            ans += 1
            mode = 0
    else:
        # check < 0
        if mode <= 0:
            mode = check
        else:
            ans += 1
            mode = 0

    prev = i

print(ans)
