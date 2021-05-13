from collections import Counter

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    counter = Counter(A)
    comb_2 = lambda n:n*(n-1)//2 if n > 1 else 0
    A_comb = sum(comb_2(v) for v in counter.values())
    # print(A_comb)
    
    for a in A:            
        q = counter[a]
        ret = A_comb -comb_2(q) + comb_2(q-1)
        
        print(ret, flush=True)
        
solve()