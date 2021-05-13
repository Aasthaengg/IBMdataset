N, H, W = map(int, input().split())
ans = 0
for _ in range(N):
    A, B = map(int, input().split())
    if A<H or B<W:
        continue
    ans += 1
print(ans)