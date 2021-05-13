from collections import defaultdict

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    
    for m in range(M):
        b, c = map(int, input().split())
        d[c] += b
        
    d = sorted(d.items(), key=lambda x: x[0], reverse=True)

    ans = 0
    for k, v in d:
        ans += min(N, v) * k
        N -= v
        if N < 0:
          break
        
    return ans

print(solve())