H,W = map(int, input().split())

a = [list(input()) for _ in range(H)]

for i in a:
    i.insert(0,'#')
    i.append('#')
    
print('#'*(W+2))
for i in a:
    print(''.join(i))
print('#'*(W+2))