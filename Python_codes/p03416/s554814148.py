def solve(n, m):

    ans = len([i for i in range(n, m+1) if str(i)[:2] == str(i)[-1:-3:-1]])
    return ans

if __name__ == "__main__":
    n, m = [int(i) for i in input().split()]
    print(solve(n, m))
