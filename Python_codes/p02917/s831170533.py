def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [B[0]]
    for i in range(N - 1):
        a = max([A[-1], B[i]])
        if i != N - 2 and a > B[i + 1]:
            a = B[i + 1]
        A.append(a)
    print(sum(A))


if __name__ == '__main__':
    main()