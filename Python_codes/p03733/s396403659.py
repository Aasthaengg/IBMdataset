N, T = map(int, input().split())
t = list(map(int, input().split()))

ans = 0
s = 0
e = T
for n in t[1:]:
    if e < n:
        ans += e - s
        s = n
    e = n + T
ans += e - s
print(ans)