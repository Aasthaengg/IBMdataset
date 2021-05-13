def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    a0 = A.pop(0)
    ans = A[1:n:2][::-1] + [a0] + A[0:n:2]
    if n % 2 == 0:
        print(' '.join([str(a) for a in ans[::-1]]))
    else:
        print(' '.join([str(a) for a in ans]))

if __name__ == '__main__':
    main()