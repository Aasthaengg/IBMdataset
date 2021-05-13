def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ret = 1
    cluester_volume = A[0]
    for a in A[1:]:
        if a <= cluester_volume*2:
            ret += 1
        else:
            ret = 1
            
        cluester_volume += a
            
    print(ret)
    
solve()