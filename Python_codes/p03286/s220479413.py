n = int(input())

A = []
if n == 0:
    print(0)
else:
    while(n != 1):
        if n % (-2) == -1:
            t = n // (-2) + 1
            n =  t
            A.append('1')
        else:
            A.append('0')
            t = n // (-2)
            n = t
    A.append(str(n))
    A = A[::-1]
    print("".join(A))