k, toayen, fromayen = map(int, input().split())
if fromayen <= toayen + 2 or k <= toayen:
    print(k + 1)
    exit()
k -= (toayen - 1)
bs = toayen
bs += (fromayen - toayen) * (k//2)
k %= 2
print(bs + 1 if k else bs)