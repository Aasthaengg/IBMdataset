a, b, c, d = map(int, input().split())
cc, dd, e = c, d, 1
for i in range(2, int(min(cc, dd)**0.5) + 1):
    if cc%i == 0 and dd%i == 0:
        while cc%i == 0 and dd%i == 0:
            cc //= i
            dd //= i
            e *= i
e *= cc*dd
print(b-a+1 - b//c + (a-1)//c - b//d + (a-1)//d + b//e - (a-1)//e)