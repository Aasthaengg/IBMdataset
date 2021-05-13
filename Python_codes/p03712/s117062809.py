h, w = map(int, input().split())
a = [input() for _ in range(h)]

print('#' * (w + 2))
for a_row in a:
    print('#' + a_row + '#')
print('#' * (w + 2))
