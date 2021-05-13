N = int(input())

def solve() :
    print(0)
    zero = input()
    
    if zero == 'Vacant' :
        return
        
    ok, ng = 0, N
    while ng - ok > 1 :
        mid = (ok + ng) // 2
        
        print(mid)
        rep = input()
        if rep == 'Vacant' :
            return
            
        if (mid % 2 == 0 and rep != zero) or (mid % 2 == 1 and rep == zero) :
            ng = mid
        else :
            ok = mid
        
solve()