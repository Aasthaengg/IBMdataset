red, green, blue, n = map(int, input().split())

ans = 0
for i in range(n // red + 1):
    for j in range(n // blue + 1):
        k = n - red * i - blue * j
        
        if k % green != 0 or k < 0:
            continue
        
        ans += 1

print(ans)