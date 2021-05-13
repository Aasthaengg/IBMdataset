X = map(int, input().split())

ans = 1

for i in X:
    if i == 0:
        print(ans)
    ans += 1