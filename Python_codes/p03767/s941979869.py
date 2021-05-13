def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    A.sort(reverse=True)

    ans = 0
    for i in range(1, 2*N, 2):
        ans += A[i]

    print(ans)

if __name__ == "__main__":
    main()