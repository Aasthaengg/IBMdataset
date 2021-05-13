def main():
    n = int(input())
    A = [0]+list(map(int, input().split()))+[0]

    S = 0
    for i in range(n+1):
        S += abs(A[i] - A[i+1])
    for i in range(1,n+1):
        print(S - abs(A[i-1]-A[i])-abs(A[i]-A[i+1]) + abs(A[i-1]-A[i+1]))


if __name__ == '__main__':
    main()
