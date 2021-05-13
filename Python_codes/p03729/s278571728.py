a, b, c = list(input().split())
ans = 'YES' if a[-1] == b[0] and b[-1] == c[0] else 'NO'
print(ans)
