n, m, c = map(int, input().split())
b = tuple(map(int, input().split()))
print(
    sum(
        sum(a * b for (b, a) in zip(b, list(map(int, input().split())))) + c > 0
        for _ in range(n)
    )
)