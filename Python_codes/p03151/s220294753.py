import bisect

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if sum(A) < sum(B):
        return -1
    
    C = [a - b for a, b in zip(A, B)]
    C.sort()
    
    mid = bisect.bisect_left(C, 0)
    minus = sum(C[:mid])
    if minus >= 0:
        return 0
    cnt = mid
    for i in reversed(range(N)):
        minus += C[i]
        cnt += 1
        if minus >= 0:
            return cnt
        
    return -1

print(solve())