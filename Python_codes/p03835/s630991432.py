k, s = map(int, input().split())
ans = 0
for z in range(0, k+1):
    sz = s-z
    for x in range(0, k+1):
        szx = sz-x
        if 0 <= szx <= k:
            ans += 1
print(ans)
