a, b = map(int,input().split())
while a != 0:
    cnt = 1
    while cnt <= a:
        if cnt%2 == 1:
            if b%2 == 0:
                print('#.'*(b//2))
            else:
                print('#.'*(b//2)+'#')
        else:
            if b%2 == 0:
                print('.#'*(b//2))
            else:
                print('.#'*(b//2)+'.')
        cnt += 1
    print()
    a, b = map(int,input().split())
