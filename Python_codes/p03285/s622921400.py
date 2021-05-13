n = int(input())

ans = False
for d in range(0, (n + 1), 7):
    if (n - d) % 4 == 0:
        ans = True
        break
print('Yes' if ans else 'No')
