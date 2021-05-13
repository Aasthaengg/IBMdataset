N, P = map(int, input().split())
odd = sum([int(i) % 2 for i in input().split()])
even = N-odd

if odd == 0:
    if P == 0:
        print(2**even)
    else:  # P==1
        print(0)
else:
    print(2**even * (2**odd//2))
