def main():
    A, B, K = map(int, input().split())

    ans = list()

    ans.extend(range(A, A+K))
    ans.extend(range(B, B-K, -1))

    ans = list(set(ans))
    ans.sort()
    for a in ans:
        if A <= a <= B:
            print(a)


if __name__ == "__main__":
    main()
