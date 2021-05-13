def main():
    # 解説AC
    N = int(input())
    AB = [[int(i) for i in input().split()] for j in range(N)]
    AB.sort(reverse=True, key=lambda p: p[0]+p[1])
    X = sum(-b for a, b in AB)
    for i in range(0, N, 2):
        X += sum(AB[i])
    print(X)


if __name__ == '__main__':
    main()
