
def solve():
    H.sort()
#    print(H)
    if K == 0:
        print(sum(H))
    else:
        print(sum(H[0:-K]))


if __name__ == "__main__":
    N,K = list(map(int, input().split()))
    H = list(map(int, input().split()))
    solve()
