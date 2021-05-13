def main():
    N = int(input())
    A = [int(i)-1 for i in input().split()]

    edge = [set() for _ in range(N)]

    for i, a in enumerate(A):
        edge[i].add(a)

    ans = 0
    for i, a in enumerate(A):
        if i in edge[a]:
            ans += 1
    print(ans//2)


if __name__ == '__main__':
    main()
