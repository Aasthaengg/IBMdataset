n, c, k = map(int, input().split())
t = sorted([int(input()) for _ in range(n)])
ans = 0
bus = 0
pk = t[0] + k

for i in range(n):
    if bus == c or t[i] > pk:
        ans += 1
        bus = 1
        pk = t[i] + k
    else: 
        bus += 1
print(ans + 1)