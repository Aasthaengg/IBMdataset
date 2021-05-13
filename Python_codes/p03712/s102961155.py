h, w = map(int, input().split())
f = ['#' for i in range(w + 2)]

print(''.join(f))

for j in range(h):
    print('#' + input() + '#')

print(''.join(f))