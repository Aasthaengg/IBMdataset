def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    C = [0]*(N+1)
    for i in range(M):
        a, b = map(int, input().split())
        C[a]+=1
        C[b]+=1
    for i in range(N+1):
        if C[i] % 2 == 1:
            return "NO"
    return "YES"

print(main())
