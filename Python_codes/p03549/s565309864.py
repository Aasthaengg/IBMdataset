def solve(n, m):

    ans = ((n-m) * 100 + 1900 * m) * 2 ** m
    return ans

if __name__ == "__main__":
    n, m = [int(i) for i in input().split()]
    print(solve(n, m))