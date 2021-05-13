n, a, b = list(map(int, input().split()))

ans = 'Borys' if (b - a) % 2 else 'Alice'

print(ans)