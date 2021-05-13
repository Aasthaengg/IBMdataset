h,w = map(int, input().split(' '))

print('#'*(w+2))
for i in range(0,h):
    print('#',end='')
    print(input(),end='')
    print('#')
print('#'*(w+2))