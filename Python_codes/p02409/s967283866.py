house = [[[0] * 10 for _ in range(3)] for __ in range(4)]

n = int(input())

while n:
    b, f, r, v = map(int, input().split())
    house[b - 1][f - 1][r - 1] += v
    n -= 1

for i, b in enumerate(house):
    for f in b:
        print(' ', end='')
        print(*f)
    if i < 3:
        print('#' * 20)