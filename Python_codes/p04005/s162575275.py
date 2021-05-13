A, B, C = map(int, input().split())

if (A*B*C)%2 == 0:
    print(0)
else:
    m = max(A,B,C)
    print(abs(((A*B*C)//m) * (m//2) - ((A*B*C)//m) * (-(-m//2))))