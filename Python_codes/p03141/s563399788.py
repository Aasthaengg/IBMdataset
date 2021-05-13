N = int(input())
AB = [list(map(int, input().split())) for i in range(N)]
D = []
for a, b in AB:
    D.append((a + b, a, b))
D.sort(reverse=True)
ans = 0
p = 0
for c, a, b in D:
    if p % 2 == 0:
        ans += a
    else:
        ans -= b
    p += 1
print(ans)
