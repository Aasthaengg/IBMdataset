def solve(M, K):
    if K == 0:
        r = [i for i in range(0, 2 ** M)]
        return " ".join(str(c) for c in r + r[::-1])
    elif M > 1 and K < (2 ** M):
        r = [i for i in range(0, (2 ** M)) if i != K]
        return " ".join(str(c) for c in r[::-1] + [K] + r + [K])
    else:
        return "-1"
 
 
if __name__ == "__main__":
    M, K = tuple(map(int, input().split(" ")))
    print(solve(M, K))