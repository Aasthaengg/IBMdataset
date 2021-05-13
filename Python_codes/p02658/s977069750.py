def main():
    N = int(input())
    A = list(map(int, input().split()))
    length = 1
    limit = 10 ** 18
    if 0 in A:
        print(0)
        return
    for i in range(N):
        length = length *  A[i]
        if length > limit:
            print('-1')
            return
    print(length)
    return
if __name__ == '__main__':
    main()