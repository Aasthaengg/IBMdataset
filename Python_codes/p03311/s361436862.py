import statistics

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(A[i]-(i+1) for i in range(N))
    B.sort()
    b = int(statistics.median(B))
    ##print(b)
    ans = 0
    for i in range(1,N+1):
        ans += abs(A[i-1]-(b+i))
    print(ans)
    ##ans2 = sum([A[i-1]-(b+i) for i in range(1,N+1)])
    ##print(ans2)

if __name__ == "__main__":
    solve()