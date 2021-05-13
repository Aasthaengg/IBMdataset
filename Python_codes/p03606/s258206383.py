# ABC073
N = int(input())
L_R = [map(int, input().split()) for _ in range(N)]
ans = 0
for l, r in L_R:
    ans += r - l + 1
print(ans)
