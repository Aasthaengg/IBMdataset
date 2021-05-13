h,w = map(int,input().split())
ary = [input() for i in range(h)]

print('#' * (w+2))

for i in range(h):
    print('#' + ary[i] + '#')

print('#' * (w+2))

