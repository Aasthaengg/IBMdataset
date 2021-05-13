a, b, c, k = map(int, input().split())
if k == 0:
    print(a - b)
else:
    a, b, c = b + c, a + c, a + b 
    if a - b <= 0:
        print(abs(a - b) * (-1) ** k)
    
    elif a - b > 0:
        print(abs(a - b) * (-1) ** (k - 1))