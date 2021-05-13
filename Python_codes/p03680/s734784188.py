N = int(input())
a = [int(input()) for _ in range(N)]
c = [True] * N
i = 0
ans = 0
while i != 1:
    if not c[i]:
        print(-1)
        exit()
    else:
        c[i] = False
        i = a[i]-1
        ans += 1
print(ans)
