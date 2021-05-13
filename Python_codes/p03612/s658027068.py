n = int(input())
p = list(map(int, input().split()))
i = 0
ans = 0
while True:
    if p[i] == i + 1:
        cnt = 0
        while p[i + cnt] == i + cnt + 1:
            cnt += 1
            if cnt + i == n:
                break
        ans += cnt//2 + cnt%2
        i += cnt
    else:
        i += 1
    if i == n:
        break
print(ans)