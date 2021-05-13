ans = 0
for A, B in [map(int, input().split()) for _ in range(int(input()))][::-1]:
    ans += (B - A - ans) % B
print(ans)
