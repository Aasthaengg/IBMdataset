n = int(input())
h = list(map(int, input().split()))
i = 0
ans = 0
c = 0
while True:
    if h[i] == 0:
        i += 1
        c += 1
        if c == n:
            break
        if i == n:
            i = 0
            c = 0
    else:
        cnt = 0
        ans += 1
        while h[i + cnt] != 0:
            h[i + cnt] -= 1
            cnt += 1
            if i + cnt == n:
                break
        i += cnt
        if i == n:
            i = 0
            c = 0
print(ans)