N, A, B = map(int, input().split())

if A > B:
    print(0)
elif N == 1 and A != B:
    print(0)
elif N == 1 and A == B:
    print(1)
elif N == 2 and A != B:
    print(1)
else:
    min_tmp = A*(N-1) + B
    max_tmp = B*(N-1) + A
    print(max_tmp-min_tmp+1)
