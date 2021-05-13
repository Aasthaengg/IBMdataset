a, b = map(int, input().split())

ans = ''
if a % 2 != b % 2:
    ans = 'IMPOSSIBLE'
else:
    ans = (a + b) // 2
print(ans)
