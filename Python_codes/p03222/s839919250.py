MOD = 1000000007
 
def get_fibonatti_table(n):
    table = [1,1]
    for i in range(2, n+1):
        table.append(table[i-1]+table[i-2])
    return table

def solve():
    H,W,K = map(int, input().split())
    fib_table = get_fibonatti_table(W)
    dp_table = [[0 for _ in range(W+1)] for _ in range(H+1)]
    dp_table[0][1] = 1
    for h in range(1, H+1):
        for w in range(1,W+1):
            weight = fib_table[w-1]*fib_table[W-w]
            dp_table[h][w] = dp_table[h-1][w] * weight
            if 1 < w:
                # w-1を足す
                weight = fib_table[w-2]*fib_table[W-w]
                # print(w,weight)
                dp_table[h][w] += dp_table[h-1][w-1] * weight
            if w < W:
                # w+1を足す
                weight = fib_table[w-1]*fib_table[W-w-1]
                dp_table[h][w] += dp_table[h-1][w+1] * weight
                
    # print(dp_table)
    print(dp_table[H][K] % MOD)
    
solve()