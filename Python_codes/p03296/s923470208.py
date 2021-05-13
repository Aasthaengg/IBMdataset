def main():
    N = int(input())
    A = list(map(int, input().split()))
    i = 0
    prev = -1
    count = 0
    while i < N:
        if prev == A[i]:
            prev = -1
            count += 1
        else:
            prev = A[i]
        i += 1
    return count

if __name__ == '__main__':
    print(main())