n = int(input())
N =[1, 1, 2]
if n < 3:
    print(N[n])
else:
    i = 2
    while i < n:
        n0, n1, n2 = N
        N[2] = n1 + n2
        N[1] = n2
        N[0] = n1
        i += 1
    print(N[2])
