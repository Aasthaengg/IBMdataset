def main():
    import sys
    N = int(input())
    C = [0] * N
    for n in range(N):
        a, b = [int(x) for x in input().strip().split()]
        C[n] = (a+b, a, b)
    C.sort(reverse=True)
    ans = 0
    for n in range(N):
        if n % 2:
            ans -= C[n][2]
        else:
            ans += C[n][1]

    print(ans)
    
if __name__ == '__main__':
    main()