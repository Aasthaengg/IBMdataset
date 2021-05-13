def solve():
    N = int(input())
    P = [int(i) for i in input().split()]
    cur = N
    ans = 0
    for num in P:
        if num <= cur:
            ans += 1
            cur = num
    print(ans)

if __name__ == "__main__":
    solve()