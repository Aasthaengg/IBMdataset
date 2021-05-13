def main():
    n = int(input())
    A = []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        A.append([a, b])
    A.sort(key = lambda x: x[0], reverse = True)
    print(sum(A[0]))


if __name__ == '__main__':
    main()
