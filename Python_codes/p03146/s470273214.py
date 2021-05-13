import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
s, = [int(num) for num in lines.pop(0).split(" ")]
count = 2
ss = set([s])
while True:
    if s % 2 == 0:
        next = s // 2
    else:
        next = 3 * s + 1
    if next in ss:
        break
    else:
        ss.add(next)
        s = next
        count += 1
print(count)
