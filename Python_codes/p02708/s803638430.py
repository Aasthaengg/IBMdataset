def main():
    mod = 10**9 +7
    n,k = map(int,input().split())
    ans = 0
    for i in range(k,n+2):
        a = i*(i-1)//2
        b = i*(2*n-i+1)//2
        ans += (b-a+1)
    print(ans%mod)
if __name__ == '__main__':
    main()