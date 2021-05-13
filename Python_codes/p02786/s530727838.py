h = int(input())
ans = 1
h //= 2
i = 2
while h > 0:
    ans += i
    i *= 2
    h //= 2
print(ans)