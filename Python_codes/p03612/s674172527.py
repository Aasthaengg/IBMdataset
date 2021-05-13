n = int(input())
p = list(map(int, input().split()))
i = 0
ans = 0
while i != n:
    if p[i] == i + 1:
        cnt = 0
        while i + cnt != n and p[i + cnt] == i + cnt + 1:
            cnt += 1
        ans += cnt//2 + cnt%2
        i += cnt
    else:
        i += 1
print(ans)