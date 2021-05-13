A, B = map(int, input().split())

ans = 0
for n in range(0, 20):
    if A * n - (n - 1) >= B:
        ans = n
        break

print(ans)