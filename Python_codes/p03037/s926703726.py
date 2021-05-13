def resolve():
    '''
    code here
    '''
    N , M = [int(item) for item in input().split()]
    LRs = [[int(item) for item in input().split()] for _ in range(M)]

    L_max = 0
    R_min = N

    for L, R in LRs:
        L_max = max(L_max, L)
        R_min = min(R_min, R)

    delta = R_min - L_max
    if delta >= 0:
        print(delta + 1)
    else:
        print(0)



if __name__ == "__main__":
    resolve()
