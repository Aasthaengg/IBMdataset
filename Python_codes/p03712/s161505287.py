H, W = map(int, input().split())
a = [input() for _ in range(H)]
print('#' * (W + 2))
for ai in a:
    print('#' + ai + '#')
print('#' * (W + 2))
