H,W = map(int, input().split())

Ans = []

for _ in range(H):
    Ans.append('#' + input() + '#')

print('#'*(W + 2))

for ans in Ans:
    print(ans)

print('#'*(W + 2))