s = input()
ans = 0
for i in s:
    ans += int(i)
    ans %= 9
print('Yes' if ans == 0 else 'No')