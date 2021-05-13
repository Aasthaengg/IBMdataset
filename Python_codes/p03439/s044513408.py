def solve():
    N = int(input())
    V = "Vacant"    
    M = "Male"
    F = "Female"

    l = 0
    r = N-1

    print(l)
    s = input()
    if s == V:
        return

    x = [F, F]
    x[s==F] = M
    
    while True:
        mid = (l+r+1)//2
        print(mid)
        s = input()
        if s == V:
            return
            
        if s == x[mid&1]:
            l = mid+1
        else:
            r = mid-1

solve()