h, a = map(int, input().split())
div, mod = divmod(h, a)
if mod == 0:
    print(div)
else:
    print(div + 1)
