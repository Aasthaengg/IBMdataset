while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    for i in range(1,a+1):
        if i == 1:
            print('#' * b)
        elif i == a:
            print('#' * b)    
        elif i != 0:
            print('#' + '.'*(b-2) + '#')
    print()