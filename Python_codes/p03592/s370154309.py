N, M, K = map(int, input().split())


def solve():
    if K == 0:
        return True
    if K % M == 0:
        return True
    if K % N == 0:
        return True

    for cr in range(N + 1):
        for cc in range(M + 1):
            count = cr * M + cc * N
            if cc > 0:
                count -= cc * cr
            if cr > 0:
                count -= cc * cr
            if count == K:
                return True
            # print(cr, cc, count)
    
    return False

if solve():
    print("Yes")
else:
    print("No")