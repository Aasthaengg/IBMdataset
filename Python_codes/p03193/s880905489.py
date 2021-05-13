def main():
    N,H,W = map(int,input().split())
    A,B = [],[]
    for _ in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        if H<=A[i] and W<=B[i]:
            ans += 1
    print(ans)
if __name__ == '__main__':
    main()