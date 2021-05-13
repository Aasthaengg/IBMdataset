def main():
    N = int(input())
    A, B = (int(i) for i in input().split())
    P = [int(i) for i in input().split()]

    cnt = [0]*3
    for p in P:
        if p <= A:
            cnt[0] += 1
        elif p <= B:
            cnt[1] += 1
        else:
            cnt[2] += 1

    print(min(cnt))


if __name__ == '__main__':
    main()
