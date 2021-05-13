n = int(input())

X = [list(map(int, input().split())) for _ in range(n)]

ans = 'No'
cnt = 0
for x1, x2 in X:
    if x1 == x2:
        cnt += 1
        if cnt == 3:
            ans = 'Yes'
            break
    else:
        cnt = 0

print(ans)
