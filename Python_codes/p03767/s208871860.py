def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort(reverse=True)
    ans = sum([A[i] for i in range(2 * N) if i % 2 == 1])
    print(ans)

if __name__ == "__main__":
    solve()