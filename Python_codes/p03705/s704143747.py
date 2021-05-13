def main():
    N, A, B = map(int, input().split())
    if A > B:
        print(0)
        return
    if N == 1:
        if A == B:
            print(1)
        else:
            print(0)
        return
    ans = (N-2) * (B-A) + 1
    print(ans)

if __name__ == "__main__":
    main()
