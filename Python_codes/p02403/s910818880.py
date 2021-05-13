y,x = [int(x) for x in input().split()]
while(x > 0 or y > 0):
    for i in range(y):
        print('#'*x)
    print()
    y,x = [int(x) for x in input().split()]