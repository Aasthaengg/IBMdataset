def yakusu(n):
    a = []
    for i in range(1, int(n*0.5)+1):
        if n % i == 0:
            a.append(i)
    a.append(n)
    return a

A, B = map(int, input().split())
b = yakusu(B)
if A in b:
    print(A + B)
else:
    print(B - A)