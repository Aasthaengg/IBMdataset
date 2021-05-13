def main():
    N = int(input())
    if N % 2 == 0:
        pair = N + 1
    else:
        pair = N
    ans = set()
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if i+j != pair:
                ans.add((i, j))
    print(len(ans))
    for a in ans:
        print(a[0], a[1])


if __name__ == "__main__":
    main()
