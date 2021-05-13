A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if V == W:
    if A == B:
        print('YES')
    else:
        print('NO')
else:
    if 0 <= abs(A-B)/(V-W) <= T:
        print('YES')
    else:
        print('NO')
