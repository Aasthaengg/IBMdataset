hw,*aaa = open(0).read().splitlines()

h,w = map(int, hw.split())

print('#'*(w+2))
for aa in aaa:
    print(f'#{aa}#')
print('#'*(w+2))