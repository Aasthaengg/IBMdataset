a,b,c,d = map(int,input().split())
B_A = abs(b - a)
C_B = abs(c - b)
C_A = abs(c - a)
if B_A <= d and C_B <=d:
    print('Yes')
elif C_A <= d:
    print('Yes')
else:
    print('No')