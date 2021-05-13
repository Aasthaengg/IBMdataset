def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cum = 0
    t = 0
    for i in range(N-1):
        cum += A[i]
        if 2*cum < A[i+1]:
            t = i+1
    ans = N - t
    print(ans)

if __name__ == "__main__":
    main()
