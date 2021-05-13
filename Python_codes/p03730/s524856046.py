A, B, C = map(int, input().split())
ans = 'NO'
for i in range(1, 1000):
    if A*i % B == C:
        ans = 'YES'
print(ans)
