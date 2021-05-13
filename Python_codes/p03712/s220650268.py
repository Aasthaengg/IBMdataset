h,w = map(int, input().split())
al = [input() for i in range(h)]
tb = '#'*(w+2)
print(tb)
for i in al:
    print('#'+i+'#')
print(tb)