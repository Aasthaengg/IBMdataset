def solve():
    N = int(input())
    L0 = 2
    L1 = 1
    if N == 1:
        print(L1)
        exit()
    Li2 = L0
    Li1 = L1
    Li = Li1 + Li2
    for _ in range(N - 2):
        Li2 = Li1
        Li1 = Li
        Li = Li1 + Li2
    print(Li)

if __name__ == "__main__":
    solve()