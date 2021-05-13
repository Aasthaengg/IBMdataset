H,W = map(int,input().split())

ikeg = '#'*(W+2)
print(ikeg)
for i in range(H):
    print('#'+input()+'#')
print(ikeg)