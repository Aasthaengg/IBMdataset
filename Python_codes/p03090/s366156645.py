def main():
    N = int(input())
    ans = []
    if N % 2 == 0:
        for i in range(1, N+1):
            for j in range(i+1, N+1):
                if i+j != N+1:
                    ans.append((i, j))
    else:
        for i in range(1, N+1):
            for j in range(i+1, N+1):
                if i+j != N:
                    ans.append((i, j))
    print(len(ans))
    for a in ans:
        print(*a)


if __name__ == '__main__':
    main()
