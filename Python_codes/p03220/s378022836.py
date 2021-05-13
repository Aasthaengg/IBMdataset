import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n, = [int(num) for num in lines.pop(0).split(" ")]
t, a = [int(num) for num in lines.pop(0).split(" ")]
h_list = [int(num) for num in lines.pop(0).split(" ")]
ans = 1
prev_dif = sys.maxsize
for index, h in enumerate(h_list, 1):
    dif = abs((t - h * 0.006) - a)
    if dif < prev_dif:
        prev_dif = dif
        ans = index
print(ans)
