n = int(input())
a = list(map(int, input().split()))

ans = 1
flg = -1
for i in range(1, n):
    if a[i-1] == a[i]:
        continue
    
    elif a[i-1] < a[i]:
        if flg == 1 or flg == -1:
            flg = 1
            continue
        else:
            ans += 1
            flg = -1

    else:
        if flg == 0 or flg == -1:
            flg = 0
            continue
        else:
            ans += 1
            flg = -1

print(ans)
