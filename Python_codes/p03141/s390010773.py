N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]
C = [[A+B, A, B] for A, B in AB]
C.sort(reverse=True)
ans = 0
for i, (c, a, b) in enumerate(C):
    if i % 2 == 0:
        ans += a
    else:
        ans -= b
print(ans)