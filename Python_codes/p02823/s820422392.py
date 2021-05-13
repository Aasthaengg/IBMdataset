n, a, b = map(int, input().split())
diff = abs(a - b)
if diff % 2 == 0:
    ans = diff // 2
else:
    ans = (diff - 1) // 2 + min(n - b, a - 1) + 1

print(ans)
