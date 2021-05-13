N = int(input())
F = []
for _ in range(N):
    f = input().split()
    fn = int("".join(f), 2)
    F.append(fn)
P = [list(map(int, input().split())) for _ in range(N)]

ans = -100000000000
for k in range(1, 2 ** 10):
    val = 0
    for i in range(N):
        c = bin(k & F[i]).count("1")
        val += P[i][c]
    ans = max(ans, val)
print(ans)
