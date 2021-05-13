def fibonacci_dp(n,lf):
    if n == 0 or n == 1:
        return lf[n]
    if n < len(lf):
        return lf[n]
    lf.insert(n,fibonacci_dp(n-2,lf) + fibonacci_dp(n-1,lf))
    return lf[n]

if __name__ == "__main__":
    n = int(input())
    lf = [1,1,]
    print(fibonacci_dp(n,lf))

