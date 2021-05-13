a, b, c = sorted(map(int, input().split()), reverse=True)
ans = (a - b) + (b - c) // 2
if (b - c) % 2 == 1:
    ans += 2
print (ans)