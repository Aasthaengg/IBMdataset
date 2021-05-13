def main():
    A = [int(input()) for _ in range(5)]
    k = int(input())
    A.sort()
    print(':(') if A[-1] - A[0] > k else print('Yay!')

if __name__ == '__main__':
    main()
