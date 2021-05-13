N, X = map(int,input().split())
L = list(map(int,input().split()))

ans, D = 1, 0
for l in L:
    D += l
    if D <= X:
        ans += 1

print(ans)