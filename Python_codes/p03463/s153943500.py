num_of_odd = num_of_even = 0
n, a, b  = map(int, input().split())

if a == 1 and b == 2:
    print('Borys')
elif a == n and b == n-1:
    print('Borys')
elif a < b:
    if (b-a) % 2:
        print('Borys')
    else:
        print('Alice')
elif a > b:
    if (a-b) % 2:
        print('Alice')
    else:
        print('Borys')