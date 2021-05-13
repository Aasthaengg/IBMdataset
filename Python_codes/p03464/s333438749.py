def calc(n, N, x):
    m, M = -1, -1
    L, R = 0, 10**13
    while L+1 < R:
        P = (L+R)//2
        if n <= x*P:
            R = P
        else:
            L = P
    if n <= x*R <= N:
        m = x*R
    L, R = 0, 10**13
    while L+1 < R:
        P = (L+R)//2
        if N < x*P:
            R = P
        else:
            L = P
    if n <= x*L <= N:
        M = x*L + (x-1)
    return m, M

def main():
    k = int(input())
    a = list(map(int, input().split()))
    f = True
    m, M = 2, 2
    for i in reversed(range(k)):
        m, M = calc(m, M, a[i])
        if m == -1 or M == -1:
            f = False
            break
    if f:
        print(m, M)
    else:
        print(-1)

if __name__ == "__main__":
    main()