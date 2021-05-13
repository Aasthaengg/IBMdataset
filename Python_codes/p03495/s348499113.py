n,k = map(int,input().split())
a = list(map(int,input().split()))

d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

d_sorted = sorted(d.items(), key = lambda x: x[1], reverse = True)

tmp = 0

for i in range(min(k, len(d_sorted))):
    tmp += d_sorted[i][1]

print(n - tmp)
