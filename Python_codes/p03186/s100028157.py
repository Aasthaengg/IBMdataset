a, b, c = map(int, input().split())

ans = 0
gedoku = a + b
if gedoku >= c-1:
    ans = b + c
else:
    can_eat_c = gedoku + 1
    ans = can_eat_c + b

print(ans)
