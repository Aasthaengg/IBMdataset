a = list(map(str,input().split()))
A = a[0]
B = a[1]
C = a[2]

if A[-1] == B[0] and B[-1] == C[0]:
    print('YES')
else:
    print('NO')
