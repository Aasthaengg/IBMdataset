k, a, b = map(int, input().split())

if a >= b-1:
    print(k+1)
else:
    if k <= a-1:
        print(k+1)
    else:
        k -= a
        k += 1
        if k % 2 == 1:
            print(k//2*(b-a)+a+1)
        else:
            print(k//2*(b-a)+a)
