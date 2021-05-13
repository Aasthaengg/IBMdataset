from collections import Counter

def solve():
    N = int(input())
    S = input()
    
    c = Counter(S)
    
    ans = 1
    for v in c.values():
        ans = ans*(v+1) % (10**9+7)
    return (ans-1) % (10**9+7)

print(solve())