A, B = map(int, input().split())

if A == B:
    print(1)
elif (A + B) % 2 == 0:
    K = (A + B) // 2
    if abs(A - K) == abs(B - K):
        print(K)
else:
    print('IMPOSSIBLE')
