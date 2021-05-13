n, a, b = map(int, input().split())

if n*a <= b:
    ans = n*a
else:
    ans = b
print(ans)