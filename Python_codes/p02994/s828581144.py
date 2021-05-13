def main():
    N, L = map(int, input().split())
    P = 0
    for i in range(1, N+1):
        P += L + i - 1
    ans = float("inf")
    for i in range(1, N+1):
        tmp = L + i - 1
        x = P - tmp
        if abs(P - x) < abs(P - ans):
            ans = x
    print(ans)

if __name__ == "__main__":
    main()