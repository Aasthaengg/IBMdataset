def main():
    N = int(input())
    A = [int(a) for a in input().split()]

    n_4 = 0
    n_2 = 0
    n_odd = 0

    for i in range(N):
        if A[i] % 4 == 0:
            n_4 += 1
        elif A[i] % 2 == 0:
            n_2 += 1
        else:
            n_odd += 1

    if (n_odd + n_2 % 2 - 1) <= n_4:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()