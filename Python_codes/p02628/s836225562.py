def main(N, K, P):
    sorted_P = sorted(P)
    ans = sum(sorted_P[:K%N]) + sum(P)*(K//N)
    return ans

if __name__ == '__main__':
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = main(N, K, P)
    print(ans)

