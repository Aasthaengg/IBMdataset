def main():
    n,k=map(int, input().split())
    A=[int(i) for i in input().split()]
    A.sort(reverse = True)

    print(sum(A[0:k]))

if __name__ == '__main__':
    main()
