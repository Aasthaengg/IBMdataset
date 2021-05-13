def main():
    N = int(input())
    T, A = map(int, input().split())
    H = [int(x) for x in input().split()]
    rec = 100000000
    ans = 0
    
    for i in range(N):
        C = T - (H[i] * 0.006)
        if C < A:
            C = A - C
        else:
            C = C - A
        if C < 0:
            C = C * (-1)
        if rec > C:
            rec = C
            ans = i + 1
    print(ans)
main()  