N, M = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(M)]
if N == 1:
    ans = 0
else:
    ans = 10 ** (N - 1)
limit = 10 ** N
while ans < limit:
    l = str(ans)
    for s, c in sc:
        if not int(l[s-1]) == c:
            break
    else:
        print(ans)
        exit()
    ans += 1
print(-1)
