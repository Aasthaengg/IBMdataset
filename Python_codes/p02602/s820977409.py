def solve():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    ans = []
    for i in range(K, N):
        if A[i - K] < A[i]:
            ans.append('Yes')
        else:
            ans.append('No')
    print('\n'.join(ans))


if __name__ == "__main__":
    solve()