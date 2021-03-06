def main():
    n = int(input())
    A, B = [None]*n, [None]*n
    for i in range(n):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    if n%2 == 0:
        p = (A[n//2-1] + A[n//2])/2
        q = (B[n//2-1] + B[n//2])/2
        print(int((q-p+0.5)*2))
    else:
        print(B[n//2] - A[n//2] + 1)

if __name__ == "__main__":
    main()