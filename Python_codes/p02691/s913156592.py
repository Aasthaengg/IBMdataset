n = int(input())
a = list(map(int, input().split()))
b = []
c = {}

ans = 0
for i in range(n):
    b.append(a[i]+i+1)
    x = -a[i]+i+1
    if x in c:
        c[x] += 1
    else:
        c[x] = 1
for i in range(n):
    if b[i] in c:
        ans += c[b[i]]
print(ans)