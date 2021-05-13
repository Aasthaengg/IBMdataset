from collections import Counter
 
 
def solve():
    N = int(input())
    D = Counter(map(int, input().split()))
    M = int(input())
    T = Counter(map(int, input().split()))
    for k, v in T.items():
        if D[k] < v:
            return 'NO'
    return 'YES'
 
 
print(solve())