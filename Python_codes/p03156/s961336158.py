# aising2019B - Contests
def main():
    n = int(input())
    A, B = list(map(int, input().rstrip().split()))
    P = sorted(map(int, input().rstrip().split()))
    a, b, c = 0, 0, 0
    for i in P:
        if i <= A:
            a += 1
        elif A < i <= B:
            b += 1
        else:
            c += 1
    print(min(a, b, c))


if __name__ == "__main__":
    main()