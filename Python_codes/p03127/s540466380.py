def main():
    N = int(input())
    A = list(map(int, input().split()))

    while True:
        A.sort()
        mod_max = 0
        for i in range(len(A)-1, 0, -1):
            tmp = A[i] % A[0]
            if tmp == 0:
                A.pop(i)
            else:
                A[i] = tmp
            if mod_max < tmp:
                mod_max = tmp
        if mod_max == 0:
            print(A[0])
            exit()
        elif mod_max == 1:
            print(1)
            exit()


if __name__ == "__main__":
    main()
