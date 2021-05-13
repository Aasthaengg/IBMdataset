import sys
def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    count = [0] * N
    for _ in range(M):
        a, b = map(int, input().split())
        a, b = min(a, b), max(a, b)
        if a > 1: count[a-1] += 1
        count[b-1] += 1
    
    for i, a in enumerate(count):
        if a % 2 > 0: 
            print("NO")
            break
    else: print("YES")

    return 0

if __name__ == "__main__":
    solve()