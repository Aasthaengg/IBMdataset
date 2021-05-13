def main():
    import bisect
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    A,B = [0],[0]
    for i in range(n):
        A.append(A[i]+a[i])
    for i in range(m):
        B.append(B[i]+b[i])
    ans = 0
    for i in range(n+1):
        left = k-A[i]
        if left>=0:
            nm = i+bisect.bisect_right(B,left)-1
            if ans<nm:
                ans = nm
    print(ans)

if __name__ == "__main__":
    main()
