def solve():
    N,C,K = map(int, input().split())
    T = [int(input()) for _ in range(N)]
    T.sort()
    
    num = 1
    bus_pos = T[0]
    ret = 1
    for t in T[1:]:
        # print(t,ret,num,bus_pos)
        if num < C and t <= bus_pos+K:
            num += 1
        else:
            ret += 1
            num = 1
            bus_pos = t
            
    print(ret)
    
solve()