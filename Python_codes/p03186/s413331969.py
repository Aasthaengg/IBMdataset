A, B, C = map(int, input().split())
if C <= B:
    print(B+C)
elif A+B<C:
    print((min(A+B, C)+1) + B)
else:
    print(B+C)