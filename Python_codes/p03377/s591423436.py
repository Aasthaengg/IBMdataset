a, b, x = map(int, input().split())
ans = 'YES' if a <= x and x <= a + b else 'NO'
print(ans)
