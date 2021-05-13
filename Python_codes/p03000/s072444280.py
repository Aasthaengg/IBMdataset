N, X = map(int, input().split())
L = list(map(int, input().split()))

m = 0
ans = 1
for l in L:
    m += l
    if m > X:
        print(ans)
        exit()
    else:
        ans += 1

print(ans)