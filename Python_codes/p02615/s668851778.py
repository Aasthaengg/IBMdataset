def main():
    N=int(input())
    A=sorted([int(_) for _ in input().split()])[::-1]
    ans = A[0]
    if N==2:
        print(ans)
    else:
        for i in range(1, N//2):
            ans += A[i]*2
        if N%2:
            ans += A[N//2]
        print(ans)
main()