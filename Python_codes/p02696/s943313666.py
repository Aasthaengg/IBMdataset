a, b, n = map(int, input().split())

ans = -1
if n < b:
    ans = (a * n // b) - a * (n // b)

else:
    ans = (a * (b-1) // b) - a * ((b-1) // b)

print(ans)
