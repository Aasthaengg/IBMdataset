a, b = map(int,input().split())
while a != 0:
    print('#'*b)
    for i in range(a-2):
        print('#'+'.'*(b-2)+'#')
    print('#'*b)
    print()
    a, b = map(int,input().split())
