import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n = int(lines.pop(0))
b_list = [int(b) for b in lines.pop(0).split(" ")]
b_list.append(sys.maxsize)
def _iter():
    prev_b = sys.maxsize
    for b in b_list:
        yield min(prev_b, b)
        prev_b = b
answer = sum(_iter())
print(answer)
