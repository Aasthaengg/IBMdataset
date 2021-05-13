def solve():
    N,K = [int(i) for i in input().split()]
    P = [int(i) for i in input().split()]
    print(sum(sorted(P)[:K]))

if __name__ == "__main__":
    solve()