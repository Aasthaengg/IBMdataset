x, k, d = map(int, input().split())
x = abs(x)
count = 0

if x - k*d > 0:
    print(x - k*d)

elif x - k*d == 0:
    print(0)

else:
    count = x//d + 1
    x -= count * d
    
    if (k - count) % 2 == 0:
        print(abs(x))
    
    else:
        print(x + d)