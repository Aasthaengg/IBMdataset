A, B, C, K = list(map(int, input().split()))
a = A
b = B
c = C

if K % 2 != 0:
    print(-a + b)
else:
    print(a - b)