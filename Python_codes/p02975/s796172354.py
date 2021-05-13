def main(): 
    n = int(input())
    a = [ int(x) for x in input().split() ]

    d = {}
    for aa in a:
        d[aa] = d.get(aa, 0) + 1

    if d.get(0, 0) == n:
        print("Yes")
        return 0
    L = sorted(list(d.items()))
    if n % 3 == 0 and len(L) == 2 and (L[0][0] == 0 and L[0][1] == n//3) and L[1][1] == n//3*2:
        print("Yes")
        return 0
    
    if n % 3 == 0 and len(L) == 3 and L[0][1] == n//3 and L[1][1] == n//3 and L[2][1] == n//3 and L[0][0]^L[1][0]^L[2][0] == 0:
        print("Yes")
        return 0

    print("No")

main()
