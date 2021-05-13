
def main():
    N = int(input())
    a = sorted(map(int, input().split()),reverse=True)      #降順のリスト

    alice = 0
    bob = 0

    for i in range(N):
        if i % 2 == 0:
            alice += a[i]

        else:
            bob += a[i]

    print(alice - bob)


if __name__ == "__main__":
    main()
