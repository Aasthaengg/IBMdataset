N, A, B = map(int, input().split())
ans = 'Borys' if (B - A) % 2 else 'Alice'
print(ans)
