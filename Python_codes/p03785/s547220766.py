n,c,k = [int(x) for x in input().split()]
t = [int(input()) for _ in range(n)]
t.sort()
bus = c
f_bus = 0
ans = 0
for i in range(n):
    if t[i] > f_bus or bus == 0:
        ans += 1
        f_bus = t[i]+k
        bus = c-1
    else:
        bus -= 1

print(ans)
