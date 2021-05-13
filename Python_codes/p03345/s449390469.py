A, B, C, K = map(int, input().split())

if K % 2 == 1:
    print(B-A)
elif K % 2 == 0:
    print(A-B)