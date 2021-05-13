a, b, n = map(int, input().split())

if n < b - 1:
    ans = (a * (n % b)) // b
else:
    ans = (a * ((b - 1) % b)) // b
print(ans)