n = int(input())
for i in range(n):
    if (i+1)**2 > n:
        break
    elif (i+1)**2 <= n:
        ans = (i + 1)**2
print(ans)