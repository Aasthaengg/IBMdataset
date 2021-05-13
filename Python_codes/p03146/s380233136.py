s = int(input())

a = {s}
b = s 
for i in range(2,1000001):
    if b%2==0:
        b //= 2
    else:
        b = 3*b+1

    if b in a:
        print(i)
        exit()
    else:
        a.add(b)