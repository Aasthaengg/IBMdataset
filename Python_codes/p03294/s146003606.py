def solve():
    _ = int(input())
    A = [int(i) for i in input().split()]
    ans = sum([a - 1 for a in A])
    print(ans)


if __name__ == "__main__":
    solve()
