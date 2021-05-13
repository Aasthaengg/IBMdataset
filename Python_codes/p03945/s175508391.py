def solve():
    S = input()
    
    d = {'B': 0, 'W': 0}
    ps = S[0]
    d[ps] += 1
    for si in S:
        if si != ps:
            d[si] += 1
        ps = si   
    return sum(d.values())-1

print(solve())