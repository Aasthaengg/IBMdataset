def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_v = min([A, B, C, D, E])
    if N % min_v != 0:
        print(4 + N // min_v + 1)
    else:
        print(4 + N // min_v)


if __name__ == '__main__':
    main()
