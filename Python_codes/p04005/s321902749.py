A, B, C = map(int, input().split())

if any(i % 2 == 0 for i in [A, B, C]):
    print(0)
else:
    print(min(A*B, B*C, C*A))