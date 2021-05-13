import sys

X = sys.stdin.readline().strip()
lx = len(X)

stack = []
pop_n = 0
for c in X:
    if c == "S":
        stack.append(c)
    elif c == "T" and 0 < len(stack):
        stack.pop()
        pop_n += 1

print(lx - 2 * pop_n)