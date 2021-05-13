def main():
    n, k = list(map(int, input().split()))
    S = list(input())
    count = 0
    h = 0
    for i in range(n - 1):
        if S[i] != S[i + 1]:
            count += 1
    b = max(0, count + 1 - 2 * k)
    print(min(n - 1, n - b))

if __name__ == '__main__':
    main()
