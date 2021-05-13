def solve():
    N, M = map(int, input().split())
    return (1900*M+100*(N-M))*2**M
    
print(solve())