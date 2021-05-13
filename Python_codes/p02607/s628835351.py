def main():
    N = int(input())
    A = [int(a) for a in input().split()]

    ans = 0
    for i in range(len(A)):
        if (i + 1) % 2 == 1 and A[i] % 2 == 1:
            ans += 1

    print(ans)
    
if __name__ == "__main__":
    main()