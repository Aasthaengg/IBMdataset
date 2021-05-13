n, m, k = list(map(int, input().split()))

flag = False
for y in range(n+1):
    if n - 2 * y == 0:
        continue
        
    x = (k - m * y) / (n - 2 * y)
    
    if (k - m * y) % (n - 2 * y) == 0 and (0 <= x and x <= m):
        flag = True
        break
print("Yes" if flag else "No")