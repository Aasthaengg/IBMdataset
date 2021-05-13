A, V = list(map(int, input().strip().split()))
B, W = list(map(int, input().strip().split()))
T = int(input().strip())

L = abs(A - B)
v = V - W

if L <= (V - W) * T:
    print('YES')
else:
    print('NO')
