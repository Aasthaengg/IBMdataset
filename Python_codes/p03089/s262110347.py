def main():
    N = int(input())
    B = [int(i) for i in input().split()]
    ans = []
    while B:
        for i in range(len(B))[::-1]:
            if B[i] == i+1:
                ans.append(B[i])
                del B[i]
                break
        else:
            return print(-1)
    print(*ans[::-1], sep="\n")


if __name__ == '__main__':
    main()
