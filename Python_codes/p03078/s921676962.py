x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
ans = []
for i in range(x):
    for j in range(y):
        for m in range(z):
            if (i+1) * (j+1) * (m+1) > k:
                break
            ans.append(a[i] + b[j] + c[m])

ans.sort(reverse=True)
for i in ans[:k]:
    print(i)