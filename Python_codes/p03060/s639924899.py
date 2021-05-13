def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    K = [V[i] - C[i] for i in range(N)]
    ans = 0
    for k in K:
        if k > 0:
            ans += k
    print(ans)


if __name__ == "__main__":
    main()
