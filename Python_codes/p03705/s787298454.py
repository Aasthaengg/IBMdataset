def main():
    N, A, B = (int(i) for i in input().split())
    if B < A or (N == 1 and A != B):
        return print(0)
    max_v = B*(N-1) + A
    min_v = A*(N-1) + B
    print(max(max_v - min_v + 1, 0))


if __name__ == '__main__':
    main()
