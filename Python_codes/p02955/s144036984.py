def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    total = sum(A)
    candidate = []
    
    for i in range(1, int(total**0.5)+1):
        if not total % i:
            candidate.extend([i, total//i])
    
    ans = 0
    
    for c in candidate:
        d = sorted([a % c for a in A])
        j = N - sum(d) // c
        
        if sum(d[:j]) <= K:
            ans = max(ans, c)
    
    print(ans)

if __name__ == '__main__':
    main()