h = int(input())
ans = 0
i = 0
while h > 0:
    h = h // 2
    ans += 2 ** i
    i += 1
print(ans)