N, A, B = map(int, input().split())
if N == 1 and A != B:
    print(0)
    exit()
elif N == 1:
    print(1)
    exit()
elif A > B:
    print(0)
    exit()
elif A == B:
    print(1)
    exit()

am = N - 2
# 最小
minv = A + B + am*A
# 最大
maxv = A + B + am*B
print(maxv - minv + 1)