def solve():
    N,T = map(int, input().split())
    A = list(map(int, input().split()))
    max_profit = 0
    min_val = 10**9
    max_profit_pair = []
    
    for a in A:
        # print(min_val, max_profit)
        if max_profit < a-min_val:
            max_profit = a-min_val
            max_profit_pair = [(min_val,a)]
        elif max_profit == a-min_val:
            max_profit_pair.append((min_val,a))
            
        if min_val > a:
            min_val = a
            
    # print(max_profit, max_profit_pair)
    print(len(max_profit_pair))
    
solve()