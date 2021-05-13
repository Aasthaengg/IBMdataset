D = [int(_) for _ in input().split()]

def solve(D):
    N = D[0]
    M = D[1]
    K = D[2]
    
    for i in range(N+1):
        for j in range(M+1):
            if (i*(M-j) + (N-i)*j) == K:
                return "Yes"

    return "No"

print(solve(D))