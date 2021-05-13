N = int(input())
t, a = map(int, input().split())

ans = t + a

for _ in range(N - 1):
    T, A = map(int, input().split())

    n = max(t // T + (1 if t % T else 0), a // A + (1 if a % A else 0))

    ans = (T + A) * n

    t, a = T * n, A * n

print(ans)
