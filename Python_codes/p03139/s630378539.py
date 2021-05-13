def main():

    N, A, B = map(int, input().split())
    max_v = min(A, B)
    min_v = max(0, A+B-N)

    print(" ".join(map(str, [max_v, min_v])))

if __name__ == '__main__':
    # print(main())
    main()