def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    op = sum(B) - sum(A)
    D = [(b-a+1)//2 if b > a else 0 for a, b in zip(A, B)]
    print("Yes" if op >= sum(D) else "No")


if __name__ == '__main__':
    main()
