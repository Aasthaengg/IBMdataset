A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if V < W:
    print('NO')
elif abs(A-B) <= abs(V-W)*T:
    print('YES')
else:
    print('NO')
