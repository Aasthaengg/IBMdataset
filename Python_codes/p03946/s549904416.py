n, t = map(int, input().split())
a = list(map(int, input().split()))

a = a[::-1]
m = [0] * n


for i in range(n):
    if i == 0:
        m[i] = a[i]
    else:
        m[i] = max(a[i], m[i-1])

a = a[::-1]
m = m[::-1]

#print(m)

sa = [0] * n
for i in range(n):
    sa[i] = m[i] - a[i]

#print(sa)

ans_max = max(sa)
ans = sa.count(ans_max)
print(ans)