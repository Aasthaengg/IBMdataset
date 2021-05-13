a, b, c = list(map(int, input().split()))

empty = a - b 

new = c - empty

if new>0:
    print(new)
else:
    print('0')