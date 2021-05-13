def solve():
    X,N = [int(i) for i in input().split()]
    if N == 0:
        print(X)
        return

    P = set([int(i) for i in input().split()])
    for i in range(len(P)+1):
        target = X - i
        if target not in P:
            print(target)
            break
        target = X + i
        if target not in P:
            print(target)
            break

if __name__ == "__main__":
    solve()