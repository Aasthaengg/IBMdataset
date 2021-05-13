n,k = map(int, input().split())
v = list(map(int, input().split()))


ans = 0

for i in range(1, k + 1):
    if i <= n:
        for j in range(i + 1):
            l = v[:j] + v[n - i + j:]
            l.sort()
            kari = sum(l)
            for x in range(min(k - i, i)):
                if l[x] >= 0:
                    break
                kari -= l[x]
            ans = max(ans, kari)

print(ans)