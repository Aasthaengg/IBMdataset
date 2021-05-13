from sys import stdin

a, b = [int(x) for x in stdin.readline().rstrip().split()]
if a < b:
    op = "<"
elif a > b:
    op = ">"
else:
    op = "=="

print("a", op, "b")
