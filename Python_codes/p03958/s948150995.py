def main():
    K, T = map(int, input().split())
    A = list(map(int, input().split()))
    max_a = max(A)
    limit = (K + 1)//2
    if max_a <= limit:
        print(0)
    else:
        remain = K - max_a
        print(max_a - remain - 1)

if __name__ == '__main__':
    main()
