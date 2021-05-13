def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    A = A[::-1]

    ans = 0
    for i in range(N-1):
        ans += A[(i+1)//2]
#        print(i//2)                                                                                   
    print(ans)


if __name__ == "__main__":
    main()




