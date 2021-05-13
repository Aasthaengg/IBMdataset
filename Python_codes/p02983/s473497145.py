L, R = map(int, input().split())

ans = 2019
for a in range(L, min(L+2019, R)+1):
    for b in range(L, min(L+2019, R)+1):
        if a == b:
            continue
        ans = min(a*b%2019, ans)
        if ans == 0:
            print(0)
            exit()
print(ans)
