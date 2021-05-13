x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort(reverse = True)
b.sort(reverse = True)
c.sort(reverse = True)
ans = []
for s in range(x):
    for t in range(y):
        if (s + 1) * (t + 1) > k:
            break
        for u in range(z):
            if (s + 1) * (t + 1) * (u + 1) > k:
                break
            ans.append(a[s] + b[t] + c[u])
ans.sort(reverse = True)
for i in range(k):
    print(ans[i])