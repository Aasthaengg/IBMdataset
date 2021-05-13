N, P = map(int, input().split())
A = list(map(int, input().split()))

# すべて偶数か判定
if all(a % 2 == 0 for a in A):
    if P == 0:
        print(2**N)
    else:
        print(0)
else:
    print(2**(N-1))