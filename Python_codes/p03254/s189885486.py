def main():
    N, x = map(int, input().split())
    A = [int(a) for a in input().split()]
    A.sort()

    ans = 0
    for i in range(len(A)):
        if i == (len(A) - 1):
            if A[i] == x:
                ans += 1

        else:
            if A[i] <= x:
                ans += 1
                x -= A[i]
    print(ans)
    
if __name__ == "__main__":
    main()