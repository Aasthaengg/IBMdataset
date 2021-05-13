H, W = map(int, input().split())
picture = [input() for _ in range(H)]
print('#' * (W + 2))
for row in picture:
    print('#' + row + '#')
print('#' * (W + 2))
