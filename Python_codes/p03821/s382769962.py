n = int(input())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append((a, b))

ans = 0
for a, b in reversed(ab):
    ans += (-a-ans)%b
print(ans)