def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    [print('Yes') if a < b else print('No') for a, b in zip(A[:n - k], A[k:])]

if __name__ == '__main__':
    main()
