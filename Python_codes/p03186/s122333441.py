a, b, c = map(int, input().split())

ans = 0
gedoku = a + b
if gedoku >= c-1:
    ans = b + c
else:
    cannot_eat = c - (gedoku+1)
    ans = c - cannot_eat + b

print(ans)
