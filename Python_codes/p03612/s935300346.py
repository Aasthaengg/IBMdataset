n = int(input())
ps = list(map(int, input().split()))
res = 0
for i in range(n):
    if ps[i] == i+1:
        if i < n - 1:
            ps[i],ps[i+1] = ps[i+1],ps[i]
            res += 1
        else:
            ps[i], ps[0] = ps[0], ps[i]
            res += 1
print(res)