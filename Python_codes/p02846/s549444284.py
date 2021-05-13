def solve():
    from sys import stdin
    f_i = stdin
    
    T1, T2 = map(int, f_i.readline().split())
    A1, A2 = map(int, f_i.readline().split())
    B1, B2 = map(int, f_i.readline().split())
    
    P = (A1 - B1) * T1
    Q = (A2 - B2) * T2
    
    if P < 0:
        P *= -1
        Q *= -1
    
    cycle = P + Q
    if cycle > 0:
        return 0
    elif cycle == 0:
        return 'infinity'
    else:
        S, T = divmod(P, -cycle)
        if T == 0:
            return 2 * S
        else:
            return 2 * S + 1

print(solve())