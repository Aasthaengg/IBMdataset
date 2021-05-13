n, t = map(int, input().split())
l = list(map(int, input().split()))
wa = t
for i in range(n - 1):
    itv = l[i + 1] - l[i]
    wa += min(t, itv)
print(wa)   