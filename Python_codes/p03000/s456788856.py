N, X = map(int, input().split())
*L, = map(int, input().split())
ans = 1
d = 0
for l in L:
    if d + l <= X:
        ans += 1
        d += l
    else:
        break
print(ans)
