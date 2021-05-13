n = int(input())
ans = False
for i in range(0, min(15, n // 7 + 1)):
    if (n - 7 * i) % 4 == 0:
        ans = True
print("Yes" if ans else "No")
