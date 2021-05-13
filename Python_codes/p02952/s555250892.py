ans = 0
for i in range(1, int(input()) + 1):
    if i <= 9 or 100 <= i <= 999 or  10000 <= i <= 99999:
        ans += 1
print(ans)

