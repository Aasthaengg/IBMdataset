def main():
    n,m = map(int,input().split())
    if abs(n-m) > 1:
        print(0)
    else:
        from math import factorial
        mod = 10**9+7
        res = factorial(n)*factorial(m)%mod
        if n == m:
            print(2*res%mod)
        else:
            print(res)
 
if __name__ == '__main__':
    main()
