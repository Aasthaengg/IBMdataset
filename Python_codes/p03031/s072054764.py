N, M = map(int, input().split())
connected = [list(map(int,input().split())) for _ in range(M)]
p = list(map(int, input().split()))
ans = 0

for i in range(1<<N):
    for j,lst in enumerate(connected):
        count = 0
        for s in lst[1:]:
            if (i>>(s-1)) & 1:
                count += 1
        if count % 2 != p[j]:
            break
    else:
        ans += 1

print(ans)
