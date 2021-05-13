n, t = map(int, input().split())
tl = list(map(int, input().split()))
ans = 0
tl.append(100000000000)
tmp = 0
for i in range(n):
    if tl[i+1] - tl[i] > t:
        ans += tl[i] - tmp + t
        tmp = tl[i+1]
    else:
        pass
print(ans)