import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n, m, c = [int(num) for num in lines.pop(0).split(" ")]
b_list = [int(num) for num in lines.pop(0).split(" ")]
def iter_a_list():
    for line in lines:
        yield [int(num) for num in line.split(" ")]

ans = 0
for a_list in iter_a_list():
    value = sum(a * b for a, b in zip(a_list, b_list))
    if value + c > 0:
        ans += 1
print(ans)
