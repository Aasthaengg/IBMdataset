def solve():
    N,K = map(int , input().split())
    A = list(map(int , input().split()))
    max_total = 22361 # sqrt(10**6 * 500)
    total = sum(A)
    search_space = set([])

    max_d = 1
    for d in range(1, min(total, max_total) ):
        if total % d == 0:
            search_space.add(d)
            search_space.add(total // d)
    
    # print(search_space)
    
    for d in search_space:
        if total % d == 0:
            remainders = [a%d for a in A]
            remainders = sorted(remainders)
            # print(d, remainders)
            positive_rem = 0
            negative_rem = 0
            flag = True
            for rem in remainders:
                if positive_rem+rem <= K:
                    positive_rem += rem
                elif negative_rem+(d-rem) <=K:
                    negative_rem += (d-rem)
                else: 
                    flag = False
                    break

            if flag and d > max_d:
                # print(d, remainders, positive_rem, negative_rem)
                max_d = d
            
    print(max_d)
    
solve()