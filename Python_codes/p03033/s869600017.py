import bisect

def solve():
    N, Q = [int(_) for _ in raw_input().split()]
    STX = []
    for i in range(N):
        Si, Ti, Xi = [int(_) for _ in raw_input().split()]
        STX.append((Si - Xi, Ti - Xi, Xi))
    D = []
    for i in range(Q):
        D.append((int(raw_input()), i))
    STX.sort(key = lambda x:x[2])
    # D have already been sorted based on settings on problem
    ans = [-1] * Q
    l = [None] * Q
    for i in range(N):
        Li, Ri, Xi = STX[i]
        lit = bisect.bisect_left(D, (Li, -1))
        rit = bisect.bisect_left(D, (Ri, -1))
        while lit < rit:
            if l[lit] is not None:
                lit = l[lit]
            else:
                ans[D[lit][1]] = Xi
                l[lit] = rit
                lit += 1
    for i in range(Q):
        print ans[i]

if __name__ == '__main__':
    solve()
