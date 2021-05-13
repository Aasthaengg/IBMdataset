N = int(input())
print(0,flush=True)
zero = input()
if zero == 'Vacant':
    exit()
l = 0
r = N-1
while True:
    if r-l <= 1:
        print(r,flush=True)
        if input() == 'Vacant':
            exit()
        print(l,flush=True)
        if input() == 'Vacant':
            exit()
    k = (r+l)//2
    print(k,flush=True)
    seat = input()
    if seat == 'Vacant':
        exit()
    else:
        if k%2:
            if seat == zero:
                r = k
            else:
                l = k
        else:
            if seat == zero:
                l = k
            else:
                r = k
