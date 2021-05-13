def solve():
    N = int(input())
    L = [0 for _ in range(N+1)]
    L[0] = 2
    L[1] = 1
    for i in range(N-1):
         L[i+2] = L[i+1] + L[i]
    print(L[N])







if __name__ == "__main__":
    solve()
