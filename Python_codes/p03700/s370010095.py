from sys import stdin
def input():
    return stdin.readline().strip()

n, a, b = map(int, input().split())
h = []
for _ in range(n):
    h.append(int(input()))

# binary search
sum_h = sum(h)

left = sum_h // (a + b*(n-1))
right = min([sum_h//a + n, max(h)//b + 1])

while left < right:
    center = (left + right) // 2

    base = center * b
    num = 0
    for i in h:
        i -= base
        if i > 0:
            num += (i - 1) // (a - b) + 1

    if num <= center:
        right = center
    else:
        left = center + 1

print(left)