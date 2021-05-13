def resolve():
    import math
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    suma = 0
    dab = 0
    dba = 0
    for i in range(n):
        suma += b[i]-a[i]
        if a[i] < b[i]:
            dab += math.ceil((b[i]-a[i])/2)
        else:
            dba += a[i]-b[i]
    if max(dba, dab) > suma:
        print("No")
    else:
        print("Yes")
resolve()