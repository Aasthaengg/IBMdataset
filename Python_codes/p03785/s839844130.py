n, c, k = map(int, input().split())
t = []
for _ in range(n):
    t.append(int(input()))
t.sort()
ans = 1
bus = 0
d_time = t[0]+k
for i in t:
    if i>d_time or bus==c:
        ans += 1
        bus = 1
        d_time = i+k
    else:
        bus += 1
print(ans)