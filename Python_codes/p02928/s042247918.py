def main():
    MOD = 10**9 + 7
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    left_smaller = [0]*N
    right_smaller = [0]*N
    for i, a in enumerate(A):
        left_smaller[i] = sum(b < a for b in A[:i])
        right_smaller[i] = sum(b < a for b in A[i+1:])

    ans = sum((l*(K)*(K-1)//2%MOD + r*(K+1)*(K)//2%MOD)%MOD for l, r in zip(left_smaller, right_smaller))%MOD
    print(ans)

if __name__ == "__main__":
    main()