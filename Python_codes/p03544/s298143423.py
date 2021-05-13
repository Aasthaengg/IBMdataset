N = int(input())

a =2
b =1

if N == 1:
    print(b)
else:
    for _ in range(1,N):
        c = b + a
        a = b
        b = c
    print(c)