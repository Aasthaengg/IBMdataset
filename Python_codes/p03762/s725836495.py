def main():
    n, m = [int(i) for i in input().split()]
    x = [int(i) for i in input().split()]
    y = [int(i) for i in input().split()]
    dx = []
    dy = []
    for i in range(n-1):
        dx.append(x[i+1]-x[i])
    for i in range(m-1):
        dy.append(y[i+1]-y[i])

    alpha = [(i+1)*(n-i-1) for i in range((n+1)//2)]
    beta = [(i+1)*(m-i-1) for i in range((m+1)//2)]

    sum_dx = sum([dx[i] * alpha[min(i, n-i-2)] for i in range(n-1)])
    sum_dy = sum([dy[i] * beta[min(i, m-i-2)] for i in range(m-1)])

    print((sum_dx * sum_dy)%(10**9+7))

main()