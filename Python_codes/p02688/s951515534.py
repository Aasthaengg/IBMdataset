def solve():
    N,K = [int(i) for i in input().split()]
    ans = set([i for i in range(1, N+1)])
    for i in range(K):
        d = int(input())
        target = set([int(j) for j in input().split()])
        ans -= target
    print(len(ans))

if __name__ == "__main__":
    solve()