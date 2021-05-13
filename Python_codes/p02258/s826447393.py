n = int(input())
stack = []
for _ in range(n):
    stack.append(int(input()))

maxv = -10**9
minv = stack[0]
for i in range(1, len(stack)):
    maxv = max(maxv, stack[i] - minv)
    minv = min(minv, stack[i])

print(maxv)