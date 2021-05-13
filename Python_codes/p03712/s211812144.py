h,w = map(int,input().split())
s = ''
for i in range(w+2):
    s += '#'
print(s)
for i in range(h):
    a = str(input())
    print('#'+a+'#')
print(s)
