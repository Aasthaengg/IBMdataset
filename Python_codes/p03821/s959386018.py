N = int(input())
inputs = reversed(tuple(tuple(map(int, input().split())) for _ in range(N)))
total = 0
for a, b in inputs:
    rem = (a + total) % b
    if rem:
        total += b - rem
print(total)