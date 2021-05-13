N = int(input())
H = list(map(int, input().split())) + [10**10]

cnt = -1
pre = 10**10
ans = -1

for h in H:
    if pre >= h:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
    pre = h
print(ans)
