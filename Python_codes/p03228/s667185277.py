from sys import stdin

a,b,c = [int(x) for x in stdin.readline().rstrip().split()]
now = 0
for i in range(c):
    if now%2 == 0:
        if a%2 == 1:
            a = (a-1)//2
            b += a
        else:
            a = a//2
            b += a
    else:
        if b%2 == 1:
            b = (b-1)//2
            a += b
        else:
            b = b//2
            a += b
    now += 1
print(a,b)