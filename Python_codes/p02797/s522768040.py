
def main():
    N, K, S = map(int, input().split())
    AS = [S] * K
    if S == pow(10, 9):
        AS1 = [1] * (N-K)
    else:
        AS1 = [S+1] * (N-K)
    ans = AS + AS1
    print(*ans)


if __name__ == "__main__":
    main()
