def main():
    k, t = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()
    print(max(0, A[-1] - 1 - sum(A[:-1])))

if __name__ == '__main__':
    main()
