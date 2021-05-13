import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n, l = [int(num) for num in lines.pop(0).split(" ")]
lower = l
upper = l + n - 1
sum = (lower + upper) * n // 2
if lower * upper > 0: # 同じ符号の場合
    if abs(lower) <= abs(upper):
        sum -= lower
    else:
        sum -= upper
print(sum)
