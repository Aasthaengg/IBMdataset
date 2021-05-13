def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = 0
    cur = 1
    for i in range(N):
        a = A[i]
        if a != cur:
            ans += 1
        else:
            cur += 1
    print(ans if ans != N else -1)

if __name__ == "__main__":
    solve()