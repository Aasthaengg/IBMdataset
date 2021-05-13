A, B, X = [int(i) for i in input().split()]

if X < A:
    print('NO')
elif (X - A) > B:
    print('NO')
else :
    print('YES')