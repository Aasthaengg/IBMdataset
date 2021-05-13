def main():
    N = int(input())
    A = [int(n) for n in input().split()]

    A = sorted(A, reverse=True)
    Alice = 0
    Bob = 0
    for i, a in enumerate(A):
        if i % 2 == 0:
            Alice += a
        else:
            Bob += a
    print(Alice - Bob)


main()
