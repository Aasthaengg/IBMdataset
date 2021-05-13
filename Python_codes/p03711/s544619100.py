import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def group(x):
    if x in [1, 3, 5, 7, 8, 10, 12]:
        return "A"
    if x in [4, 6, 9, 11]:
        return "B"
    if x in [2]:
        return "C"


x, y = map(int, readline().split())
ans = 'Yes' if group(x) == group(y) else 'No'
print(ans)