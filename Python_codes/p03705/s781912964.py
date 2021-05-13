import sys
N, A, B = map(int, input().split())
if A > B:
    print(0)
    sys.exit()
if N == 1:
    if A != B:
        print(0)
        sys.exit()
    else:
        print(1)
        sys.exit()
else:
    mn = A*(N-1) + B
    mx = A + B*(N-1)
    ans =mx -mn + 1
    print(ans)
