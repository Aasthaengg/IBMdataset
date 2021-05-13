import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n, = [int(num) for num in lines.pop(0).split(" ")]
price_list = [int(num) for num in lines]
ans = sum(price_list) - max(price_list) // 2
print(ans)
