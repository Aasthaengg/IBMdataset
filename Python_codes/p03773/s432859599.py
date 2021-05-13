a, b = list(map(int, input().split()))

c = a + b 

if c < 24:
    print(c)
elif c == 24:
    print('0')
else:
    print(c-24)