H,W=map(int,input().split())
lines = []
for _ in range(H):
    lines.append(input())

print('#'*(W+2))
for line in lines:
    print('#' + line + '#')
print('#'*(W+2))
