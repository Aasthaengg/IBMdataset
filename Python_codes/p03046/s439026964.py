m, k = map(int, input().split())

if k >= 2**m:
    print(-1)
    exit()
if m == 0:
    if k == 0:
        print(0, 0)
    else:
        print(-1)
    exit()
if m == 1:
    if k == 0:
        print(0, 0, 1, 1)
    else:
        print(-1)
    exit()

x, y = [i for i in range(k)], [j for j in range(k+1, 2**m)]
l = x+y
r = list(reversed(l))
ans = l+[k]+r+[k]
print(*ans)
