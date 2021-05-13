def main():
    N = int(input())
    T = list(map(int, input().split()))
    M = int(input())
    ans = []
    for _ in range(M):
        P, X = map(int, input().split())
        ans.append(str(sum(T) - T[P - 1] + X))
    print("\n".join(ans))


if __name__ == '__main__':
    main()
