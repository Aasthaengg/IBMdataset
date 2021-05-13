h, w = map(int, input().split())
for i in range(h+2):
    if i == 0 or i == h+1:
        print('#' * (w+2))
    else:
        print('#' + input() + '#')