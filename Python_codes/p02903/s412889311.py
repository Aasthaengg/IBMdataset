import sys
h, w, a, b = [int(i) for i in sys.stdin.readline().split()]
res = []
res.append(("0" * a + "1" * (w - a) + "\n") * b)
res.append(("1" * a + "0" * (w - a) + "\n") * (h-b))
print("".join(res))