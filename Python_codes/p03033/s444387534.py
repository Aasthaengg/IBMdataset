
def BinarySearchLowerBound(_arr, _ele): # arr is strictly increasing
    low_ind = 0
    up_ind = len(_arr) - 1
    if _arr[low_ind] >= _ele:
        return low_ind
    if _arr[up_ind] <= _ele:
        return up_ind + 1
    found = None
    while (up_ind - low_ind) > 1:
        mid = (up_ind + low_ind) / 2
        if _arr[mid] < _ele:
            low_ind = mid
        elif _arr[mid] > _ele:
            up_ind = mid
        elif _arr[mid] == _ele:
            found = mid
            break
    if found is not None:
        cnt = found
    else:
        cnt = up_ind
    return cnt

def solve():
    N, Q = [int(_) for _ in raw_input().split()]
    STX = []
    for i in range(N):
        Si, Ti, Xi = [int(_) for _ in raw_input().split()]
        STX.append((Si - Xi, Ti - Xi, Xi))
    D = []
    for i in range(Q):
        D.append(int(raw_input()))
    STX.sort(key = lambda x:x[2])
    # D have already been sorted based on settings on problem
    ans = [-1] * Q
    l = [None] * Q
    for i in range(N):
        Li, Ri, Xi = STX[i]
        if len(D) == 0:
            break
        lit = BinarySearchLowerBound(D, Li)
        rit = BinarySearchLowerBound(D, Ri)
        while lit < rit:
            if l[lit] is not None:
                lit = l[lit]
            else:
                ans[lit] = Xi
                l[lit] = rit
                lit += 1
    for i in range(Q):
        print ans[i]

if __name__ == '__main__':
    solve()
