n = int(input())
ans = (n) // 11
n -= ans * 11
if n == 0:
    print(ans * 2)
else:
    print(ans * 2 + 1 + (n > 6))
