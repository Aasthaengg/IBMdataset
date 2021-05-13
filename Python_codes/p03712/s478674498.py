h, w = map(int, input().split())
a = list(input() for _ in range(h))

print('#'*(w+2))
for i in a:
    ans = '#'+i+'#'
    print(ans)
print('#'*(w+2))
